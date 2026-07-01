from datetime import datetime

from app.core.exceptions import VectorStoreException


class VectorMetadataProcessor:
    """
    Adds vector database metadata.
    """

    @staticmethod
    def process(
        metadata: dict
    ) -> dict:

        try:

            metadata.update(
                {
                    "vector_store": "ChromaDB",
                    "indexed_at": datetime.now().isoformat()
                }
            )

            return metadata

        except Exception as exception:

            raise VectorStoreException(
                "Failed to update vector metadata."
            ) from exception