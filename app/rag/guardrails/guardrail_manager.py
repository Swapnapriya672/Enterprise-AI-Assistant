from langchain_core.documents import Document

from app.rag.guardrails.relevance_guard import (
    RelevanceGuard,
)


class GuardrailManager:
    """
    Enterprise Guardrail Pipeline.
    """

    def validate(
        self,
        results: list[tuple[Document, float]]
    ) -> bool:

        return RelevanceGuard.is_relevant(
            results
        )