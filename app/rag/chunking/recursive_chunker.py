from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.exceptions import ChunkingException
from app.rag.chunking.base_chunker import BaseChunker


class RecursiveChunker(BaseChunker):
    """
    Recursive text chunker.
    """

    def chunk(
        self,
        documents: list[Document]
    ) -> list[Document]:

        try:

            splitter = RecursiveCharacterTextSplitter(

                chunk_size=self.chunk_size,

                chunk_overlap=self.chunk_overlap,

                separators=[
                    "\n\n",
                    "\n",
                    " ",
                    ""
                ]
            )

            return splitter.split_documents(documents)

        except Exception as exception:

            raise ChunkingException(
                "Failed to chunk documents."
            ) from exception