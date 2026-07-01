from langchain_core.documents import Document

from app.core.exceptions import ChunkingException

from app.rag.chunking.chunk_metadata import (
    ChunkMetadataProcessor,
)

from app.rag.chunking.recursive_chunker import (
    RecursiveChunker,
)

from app.config.settings import (
    CHUNK_SIZE,
    CHUNK_OVERLAP,
)



class ChunkManager:
    """
    Main chunking pipeline.
    """

    def __init__(

            self,

            chunk_size=CHUNK_SIZE,

            chunk_overlap=CHUNK_OVERLAP

        ):

        self.chunker = RecursiveChunker(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def process(
        self,
        documents: list[Document]
    ) -> list[Document]:

        try:

            chunked_documents = self.chunker.chunk(
                documents
            )

            chunked_documents = (
                ChunkMetadataProcessor.process(
                    chunked_documents
                )
            )

            return chunked_documents

        except Exception as exception:

            raise ChunkingException(
                "Failed to process document chunking."
            ) from exception