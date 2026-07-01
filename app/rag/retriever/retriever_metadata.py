from datetime import datetime

from langchain_core.documents import Document

from app.core.exceptions import RetrieverException


class RetrieverMetadataProcessor:
    """
    Adds retrieval metadata to retrieved documents.
    """

    @staticmethod
    def process(
        documents: list[Document]
    ) -> list[Document]:

        try:

            for rank, document in enumerate(documents, start=1):

                document.metadata.update(
                    {
                        "retrieval_rank": rank,
                        "retrieved_at": datetime.now().isoformat()
                    }
                )

            return documents

        except Exception as exception:

            raise RetrieverException(
                "Failed to process retrieval metadata."
            ) from exception