from langchain_core.documents import Document

from app.core.exceptions import RetrieverException

from app.rag.retriever.similarity_retriever import (
    SimilarityRetriever,
)

from app.rag.retriever.retriever_metadata import (
    RetrieverMetadataProcessor,
)

from app.config.settings import TOP_K

class RetrieverManager:
    """
    Main retrieval pipeline.
    """

    def __init__(self):

        self.retriever = SimilarityRetriever()

    def retrieve(
        self,
        query: str,
        k: int = TOP_K
    ) -> list[Document]:

        try:

            documents = self.retriever.retrieve(
                query=query,
                k=k
            )

            documents = RetrieverMetadataProcessor.process(
                documents
            )

            return documents

        except Exception as exception:

            raise RetrieverException(
                "Failed to retrieve relevant documents."
            ) from exception