import re

from langchain_core.documents import Document

from app.core.exceptions import PreprocessingException


class TextCleaner:
    """
    Cleans the text content of LangChain documents.
    """

    @staticmethod
    def clean(document: Document) -> Document:

        try:

            text = document.page_content

            text = re.sub(
                r"\s+",
                " ",
                text
            )

            text = re.sub(
                r"\n{2,}",
                "\n",
                text
            )

            text = text.replace(
                "\t",
                " "
            )

            document.page_content = text.strip()

            return document

        except Exception as exception:

            raise PreprocessingException(
                "Failed to clean document text."
            ) from exception