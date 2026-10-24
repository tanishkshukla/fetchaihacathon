"""
CampusMitra AI - ChromaDB Vector Store & Retriever
Stores chunked PDF college documents in ChromaDB with embeddings for semantic retrieval.
Includes a graceful fallback search engine if running in restricted environments.
"""
import os
import math
import re
from typing import List, Dict, Optional
import chromadb
from chromadb.config import Settings

from .pdf_extractor import extract_text_from_pdf, chunk_text

DEFAULT_CHROMA_DIR = os.path.join(os.path.dirname(__file__), "chroma_db")


class CampusVectorStore:
    def __init__(self, persist_dir: str = DEFAULT_CHROMA_DIR):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)
        self.client = None
        self.collection = None
        self.fallback_chunks = []
        self._init_chroma()

    def _init_chroma(self):
        try:
            self.client = chromadb.PersistentClient(path=self.persist_dir)
            self.collection = self.client.get_or_create_collection(
                name="campus_documents",
                metadata={"description": "CITS College Handbook, Rules, Timetables & Directory"}
            )
            print("[CHROMA] Connected to persistent ChromaDB at:", self.persist_dir)
        except Exception as e:
            print(f"[CHROMA WARNING] Could not initialize PersistentClient ({e}). Using in-memory fallback.")
            self.client = None
            self.collection = None

    def ingest_pdf(self, pdf_path: str) -> int:
        """
        Extracts, chunks, and indexes a PDF document into ChromaDB.
        """
        docs = extract_text_from_pdf(pdf_path)
        chunks = chunk_text(docs)
        self.fallback_chunks.extend(chunks)

        if not chunks:
            return 0

        if self.collection:
            ids = [c["id"] for c in chunks]
            documents = [c["text"] for c in chunks]
            metadatas = [{"page": c["page"], "source": c["source"]} for c in chunks]

            try:
                # Upsert chunks into ChromaDB
                self.collection.upsert(
                    ids=ids,
                    documents=documents,
                    metadatas=metadatas
                )
                print(f"[CHROMA] Ingested {len(chunks)} chunks into collection 'campus_documents'.")
            except Exception as err:
                print(f"[CHROMA ERROR] Upsert failed ({err}). Storing in fallback cache.")
        return len(chunks)

    def search(self, query: str, n_results: int = 3) -> List[Dict[str, any]]:
        """
        Retrieves top-N relevant document chunks for a given user query.
        """
        if self.collection and self.collection.count() > 0:
            try:
                results = self.collection.query(
                    query_texts=[query],
                    n_results=min(n_results, self.collection.count())
                )
                hits = []
                docs = results.get("documents", [[]])[0]
                metas = results.get("metadatas", [[]])[0]
                dists = results.get("distances", [[]])[0] if "distances" in results else [0.0] * len(docs)

                for doc_text, meta, dist in zip(docs, metas, dists):
                    hits.append({
                        "text": doc_text,
                        "page": meta.get("page", 1),
                        "source": meta.get("source", "campus_handbook.pdf"),
                        "score": round(1.0 - float(dist), 3) if dist is not None else 1.0
                    })
                if hits:
                    return hits
            except Exception as e:
                print(f"[CHROMA QUERY ERROR] {e}. Falling back to keyword search.")

        # Fallback keyword/token match
        return self._fallback_search(query, n_results)

    def _fallback_search(self, query: str, n_results: int = 3) -> List[Dict[str, any]]:
        q_tokens = set(re.findall(r'\w+', query.lower()))
        scored = []
        for c in self.fallback_chunks:
            chunk_tokens = set(re.findall(r'\w+', c["text"].lower()))
            overlap = len(q_tokens.intersection(chunk_tokens))
            if overlap > 0:
                score = overlap / math.sqrt(len(q_tokens) * len(chunk_tokens) + 1)
                scored.append((score, c))

        scored.sort(key=lambda x: x[0], reverse=True)
        return [
            {
                "text": item["text"],
                "page": item["page"],
                "source": item["source"],
                "score": round(sc, 3)
            }
            for sc, item in scored[:n_results]
        ]


# Singleton instance
_store = None

def get_vector_store() -> CampusVectorStore:
    global _store
    if _store is None:
        _store = CampusVectorStore()
        # Ingest handbook PDF if present
        handbook_path = os.path.join(os.path.dirname(__file__), "..", "data", "campus_handbook.pdf")
        if os.path.exists(handbook_path):
            _store.ingest_pdf(handbook_path)
    return _store
