from datetime import datetime

from app.core.exceptions import EmbeddingException


class EmbeddingMetadataProcessor:
    """
    Processes embedding metadata.
    """

    @staticmethod
    def process(
        metadata: dict
    ) -> dict:

        try:

            metadata.update(
                {
                    "embedding_model":
                    "sentence-transformers/all-MiniLM-L6-v2",

                    "embedding_dimension": 384,

                    "embedded_at":
                    datetime.now().isoformat()
                }
            )

            return metadata

        except Exception as exception:

            raise EmbeddingException(
                "Failed to process embedding metadata."
            ) from exception