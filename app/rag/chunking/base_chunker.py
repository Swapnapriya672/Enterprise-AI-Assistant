from abc import ABC, abstractmethod

from langchain_core.documents import Document

from app.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)


class BaseChunker(ABC):
    """
    Base class for all document chunkers.
    """

    def __init__(
        self,
        chunk_size: int = CHUNK_SIZE,
        chunk_overlap: int = CHUNK_OVERLAP
    ):

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    @abstractmethod
    def chunk(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split documents into chunks.
        """
        pass