from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings

from app.core.exceptions import EmbeddingException
from app.rag.embeddings.base_embedding import BaseEmbedding
from app.config.settings import EMBEDDING_MODEL


class HuggingFaceEmbedding(BaseEmbedding):
    """
    HuggingFace embedding model.
    """

    MODEL_NAME = EMBEDDING_MODEL

    def __init__(self):

        self.embedding_model = HuggingFaceEmbeddings(
            model_name=self.MODEL_NAME
        )

    def embed_documents(
        self,
        documents: list[Document]
    ) -> list[list[float]]:

        try:

            texts = [

                document.page_content

                for document in documents

            ]

            return self.embedding_model.embed_documents(
                texts
            )

        except Exception as exception:

            raise EmbeddingException(
                "Failed to generate document embeddings."
            ) from exception

    def embed_query(
        self,
        query: str
    ) -> list[float]:

        try:

            return self.embedding_model.embed_query(
                query
            )

        except Exception as exception:

            raise EmbeddingException(
                "Failed to generate query embedding."
            ) from exception