from langchain_core.documents import Document

from app.core.exceptions import EmbeddingException

from app.rag.embeddings.embedding_metadata import (
    EmbeddingMetadataProcessor,
)

from app.rag.embeddings.huggingface_embedding import (
    HuggingFaceEmbedding,
)


class EmbeddingManager:
    """
    Main embedding pipeline.
    """

    def __init__(self):

        self.embedding_model = HuggingFaceEmbedding()

    def process(
        self,
        documents: list[Document]
    ) -> tuple[list[Document], list[list[float]]]:

        try:

            embeddings = self.embedding_model.embed_documents(
                documents
            )

            for document in documents:

                document.metadata = (
                    EmbeddingMetadataProcessor.process(
                        document.metadata
                    )
                )

            return documents, embeddings

        except Exception as exception:

            raise EmbeddingException(
                "Failed to generate embeddings."
            ) from exception

    def embed_query(
        self,
        query: str
    ) -> list[float]:

        return self.embedding_model.embed_query(query)