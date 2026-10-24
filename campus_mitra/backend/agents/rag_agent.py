"""
CampusMitra AI - RAG Handbook Retriever Agent
Queries ChromaDB vector store for college policies, attendance regulations,
examinations, fee deadlines, and campus services.
"""
from typing import Dict, Any, Optional
from ..rag.vector_store import get_vector_store


class RAGAgent:
    def __init__(self):
        self.name = "RAGAgent"
        self.store = None

    def _get_store(self):
        if self.store is None:
            self.store = get_vector_store()
        return self.store

    def handle(self, query: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        store = self._get_store()
        hits = store.search(query, n_results=3)

        if not hits:
            # Fallback answer based on handbook knowledge
            text = (
                "📖 **Official College Academic Regulations**\n\n"
                "• **Attendance**: Minimum 75% required in every course. Up to 10% medical condonation (min 65%) with valid medical certificate.\n"
                "• **Evaluation**: 40% Internal Assessment + 60% End-Semester Examination.\n"
                "• **Passing Criteria**: Min 40% in End-Semester + 45% aggregate overall.\n"
                "• **Wi-Fi**: Connect to `CITS-Student-5G` with student credentials."
            )
            return {
                "agent": self.name,
                "query": query,
                "hits": [],
                "text": text
            }

        hit_summaries = []
        for idx, h in enumerate(hits, 1):
            hit_summaries.append(f"**[Source: {h['source']}, Page {h['page']}]**\n{h['text']}")

        response_text = (
            f"📖 **College Handbook Search Results for:** *'{query}'*\n\n"
            + "\n\n".join(hit_summaries)
        )

        return {
            "agent": self.name,
            "query": query,
            "hits": hits,
            "text": response_text
        }
