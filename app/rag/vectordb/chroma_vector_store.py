from langchain_core.documents import Document
from langchain_chroma import Chroma

from app.core.exceptions import VectorStoreException
from app.rag.embeddings.huggingface_embedding import HuggingFaceEmbedding
from app.rag.vectordb.base_vector_store import BaseVectorStore
from app.config.settings import VECTOR_STORE_PATH


class ChromaVectorStore(BaseVectorStore):
    """
    Chroma vector database implementation.
    """

    def __init__(
        self,
        persist_directory=str(VECTOR_STORE_PATH)
    ):

        embedding_model = HuggingFaceEmbedding()

        self.vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding_model.embedding_model
        )

    def add_documents(
        self,
        documents: list[Document]
    ) -> None:

        try:

            self.vector_store.add_documents(
                documents
            )

        except Exception as exception:

            raise VectorStoreException(
                "Failed to store documents."
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