from langchain_core.documents import Document

from app.core.exceptions import VectorStoreException

from app.rag.vectordb.chroma_vector_store import (
    ChromaVectorStore,
)

from app.rag.vectordb.vector_metadata import (
    VectorMetadataProcessor,
)


class VectorStoreManager:
    """
    Main vector database pipeline.
    """

    def __init__(self):

        self.vector_store = ChromaVectorStore()

    def index_documents(
        self,
        documents: list[Document]
    ) -> None:

        try:

            for document in documents:

                document.metadata = (
                    VectorMetadataProcessor.process(
                        document.metadata
                    )
                )

            self.vector_store.add_documents(
                documents
            )

        except Exception as exception:

            raise VectorStoreException(
                "Failed to index documents."
            ) from exception

    def similarity_search(
        self,
        query: str,
        k: int = 5
    ) -> list[Document]:

        try:

            return self.vector_store.similarity_search(
                query=query,
                k=k
            )

        except Exception as exception:

            raise VectorStoreException(
                "Similarity search failed."
            ) from exception

    def similarity_search_with_score(
        self,
        query: str,
        k: int = 5
    ) -> list[tuple[Document, float]]:

        try:

            return self.vector_store.similarity_search_with_score(
                query=query,
                k=k
            )

        except Exception as exception:

            raise VectorStoreException(
                "Similarity search with score failed."
            ) from exception