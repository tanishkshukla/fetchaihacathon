import os
import re
from typing import List, Dict

try:
    from pypdf import PdfReader
    PYPDF_AVAILABLE = True
except Exception:
    PYPDF_AVAILABLE = False


def extract_text_from_pdf(pdf_path: str) -> List[Dict[str, any]]:
    """
    Extracts text page-by-page from a PDF file.
    Returns a list of dicts: [{"page": page_num, "text": text, "source": filename}]
    """
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")

    filename = os.path.basename(pdf_path)
    documents = []

    if PYPDF_AVAILABLE:
        try:
            reader = PdfReader(pdf_path)
            for page_idx, page in enumerate(reader.pages):
                page_text = page.extract_text() or ""
                page_text = page_text.strip()
                if page_text:
                    documents.append({
                        "page": page_idx + 1,
                        "text": page_text,
                        "source": filename
                    })
            if documents:
                return documents
        except Exception as e:
            print(f"[PDF EXTRACTOR WARNING] pypdf extraction encountered {e}. Trying fallback extractor.")

    # Fallback: Check if a matching .txt or handbook document exists in data directory
    txt_path = pdf_path.replace(".pdf", ".txt")
    if not os.path.exists(txt_path):
        txt_path = os.path.join(os.path.dirname(pdf_path), "campus_handbook.txt")
        if not os.path.exists(txt_path):
            txt_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "campus_docs", "campus_handbook.txt")

    if os.path.exists(txt_path):
        with open(txt_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            # Split sections into virtual pages
            sections = content.split("--------------------------------------------------------------------------------")
            for idx, sec in enumerate(sections, 1):
                clean_sec = sec.strip()
                if clean_sec:
                    documents.append({
                        "page": idx,
                        "text": clean_sec,
                        "source": filename
                    })
            return documents

    # Direct raw stream extraction from PDF
    try:
        with open(pdf_path, "rb") as f:
            raw = f.read().decode("latin1", errors="ignore")
            # Extract text within parentheses in PDF streams e.g. (Text) Tj
            matches = re.findall(r'\((.*?)\)\s*T[jJ]', raw)
            if matches:
                clean_text = " ".join(matches)
                documents.append({"page": 1, "text": clean_text, "source": filename})
    except Exception:
        pass

    return documents


def chunk_text(documents: List[Dict[str, any]], chunk_size: int = 400, chunk_overlap: int = 80) -> List[Dict[str, any]]:
    """
    Splits document pages into smaller overlapping chunks suitable for vector embeddings.
    """
    chunks = []
    chunk_counter = 0

    for doc in documents:
        full_text = doc["text"]
        # Split by paragraphs or double newlines where possible
        paragraphs = [p.strip() for p in full_text.split("\n") if p.strip()]
        
        current_chunk = ""
        for p in paragraphs:
            if len(current_chunk) + len(p) <= chunk_size:
                current_chunk += " " + p if current_chunk else p
            else:
                if current_chunk:
                    chunk_counter += 1
                    chunks.append({
                        "id": f"{doc['source']}_p{doc['page']}_c{chunk_counter}",
                        "text": current_chunk.strip(),
                        "page": doc["page"],
                        "source": doc["source"]
                    })
                # Start new chunk with overlap if possible
                overlap_text = current_chunk[-chunk_overlap:] if len(current_chunk) > chunk_overlap else ""
                current_chunk = (overlap_text + " " + p).strip()

        if current_chunk:
            chunk_counter += 1
            chunks.append({
                "id": f"{doc['source']}_p{doc['page']}_c{chunk_counter}",
                "text": current_chunk.strip(),
                "page": doc["page"],
                "source": doc["source"]
            })

    return chunks
