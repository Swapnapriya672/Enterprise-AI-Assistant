from langchain_core.documents import Document

from app.core.exceptions import PipelineException


class RelevanceGuard:
    """
    Checks whether retrieved documents are relevant.
    """

    MIN_SCORE = 1.50

    @staticmethod
    def is_relevant(
        results: list[tuple[Document, float]]
    ) -> bool:

        try:

            if not results:

                return False

            best_score = results[0][1]

            return best_score <= RelevanceGuard.MIN_SCORE

        except Exception as exception:

            raise PipelineException(
                "Failed to validate retrieval relevance."
            ) from exception