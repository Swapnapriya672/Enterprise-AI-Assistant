from langchain_core.documents import Document

from app.core.exceptions import ChunkingException


class ChunkMetadataProcessor:
    """
    Adds metadata to each chunk.
    """

    @staticmethod
    def process(
        documents: list[Document]
    ) -> list[Document]:

        try:

            for index, document in enumerate(documents):

                document.metadata.update(
                    {
                        "chunk_id": index + 1,
                        "chunk_size": len(
                            document.page_content
                        )
                    }
                )

            return documents

        except Exception as exception:

            raise ChunkingException(
                "Failed to process chunk metadata."
            ) from exception