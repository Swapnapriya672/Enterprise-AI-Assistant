from langchain_core.documents import Document

from app.core.exceptions import RetrieverException
from app.rag.vectordb.vector_store_manager import VectorStoreManager
from app.rag.retriever.base_retriever import BaseRetriever
from app.config.settings import TOP_K


class SimilarityRetriever(BaseRetriever):
    """
    Performs similarity search using the vector store.
    """

    def __init__(self):

        self.vector_store = VectorStoreManager()

    def retrieve(
        self,
        query: str,
        k: int = TOP_K
    ) -> list[Document]:

        try:

            return self.vector_store.similarity_search(
                query=query,
                k=k
            )

        except Exception as exception:

            raise RetrieverException(
                "Failed to retrieve documents."
            ) from exception