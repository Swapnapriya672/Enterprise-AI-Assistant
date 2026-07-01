from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class MarkdownLoader(BaseLoader):
    """
    Loader for Markdown documents.
    """

    def load(self) -> list[Document]:

        markdown_documents = []

        try:

            markdown_files = self.documents_path.glob("*.md")

            for markdown_file in markdown_files:

                with open(
                    markdown_file,
                    mode="r",
                    encoding="utf-8"
                ) as file:

                    content = file.read()

                metadata = self.create_metadata(
                    file_path=markdown_file,
                    document_type="Markdown Document"
                )

                document = Document(
                    page_content=content,
                    metadata=metadata
                )

                markdown_documents.append(document)

            return markdown_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load Markdown documents."
            ) from exception