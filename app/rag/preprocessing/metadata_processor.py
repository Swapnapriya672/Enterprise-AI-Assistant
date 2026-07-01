from datetime import datetime

from langchain_core.documents import Document

from app.core.exceptions import PreprocessingException


class MetadataProcessor:
    """
    Enriches document metadata.
    """

    @staticmethod
    def process(
        document: Document
    ) -> Document:

        try:

            document.metadata.update(
                {
                    "character_count": len(
                        document.page_content
                    ),

                    "word_count": len(
                        document.page_content.split()
                    ),

                    "line_count": len(
                        document.page_content.splitlines()
                    ),

                    "processed_timestamp": datetime.now().isoformat()
                }
            )

            return document

        except Exception as exception:

            raise PreprocessingException(
                "Failed to process metadata."
            ) from exception