from langchain_core.documents import Document

from app.core.exceptions import RetrievalException

from app.rag.vectordb.vector_store_manager import (
    VectorStoreManager,
)


class RetrieverManager:
    """
    Main retrieval pipeline.
    """

    def __init__(self):

        self.vector_store = VectorStoreManager()

    def retrieve(
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

            raise RetrievalException(
                "Document retrieval failed."
            ) from exception

    def retrieve_with_scores(
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

            raise RetrievalException(
                "Document retrieval with scores failed."
            ) from exception