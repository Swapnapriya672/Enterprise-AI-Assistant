from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseEmbedding(ABC):
    """
    Base class for embedding models.
    """

    @abstractmethod
    def embed_documents(
        self,
        documents: list[Document]
    ) -> list[list[float]]:
        """
        Generate embeddings for documents.
        """
        pass

    @abstractmethod
    def embed_query(
        self,
        query: str
    ) -> list[float]:
        """
        Generate embedding for a query.
        """
        pass