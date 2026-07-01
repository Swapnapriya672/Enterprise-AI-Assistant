from app.core.exceptions import PipelineException

from app.config.settings import DOCUMENTS_PATH

from app.rag.loaders.document_loader import DocumentLoader
from app.rag.preprocessing.preprocessor import Preprocessor
from app.rag.chunking.chunk_manager import ChunkManager
from app.rag.vectordb.vector_store_manager import VectorStoreManager


class IndexingPipeline:
    """
    Complete document indexing pipeline.
    """

    def __init__(self):

        self.loader = DocumentLoader(
            str(DOCUMENTS_PATH)
        )

        self.preprocessor = Preprocessor()

        self.chunk_manager = ChunkManager()

        self.vector_store = VectorStoreManager()

    def run(self):

        try:

            documents = self.loader.load()

            documents = self.preprocessor.process(
                documents
            )

            documents = self.chunk_manager.process(
                documents
            )

            self.vector_store.index_documents(
                documents
            )

            return {
                "status": "success",
                "documents_indexed": len(documents)
            }

        except Exception as exception:

            raise PipelineException(
                "Indexing pipeline failed."
            ) from exception