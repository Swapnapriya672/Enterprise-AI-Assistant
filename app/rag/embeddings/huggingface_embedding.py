from langchain_huggingface import HuggingFaceEmbeddings

from app.config.settings import EMBEDDING_MODEL

from app.core.exceptions import EmbeddingException


class HuggingFaceEmbedding:
    """
    Singleton HuggingFace embedding model.
    """

    _embedding_model = None

    def __init__(self):

        try:

            if HuggingFaceEmbedding._embedding_model is None:

                print("Loading Embedding Model...")

                HuggingFaceEmbedding._embedding_model = (
                    HuggingFaceEmbeddings(
                        model_name=EMBEDDING_MODEL
                    )
                )

            self.embedding_model = (
                HuggingFaceEmbedding._embedding_model
            )

        except Exception as exception:

            raise EmbeddingException(
                "Failed to initialize embedding model."
            ) from exception