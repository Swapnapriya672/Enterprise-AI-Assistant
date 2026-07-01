from langchain_core.documents import Document

from app.core.exceptions import PreprocessingException


class DocumentValidator:
    """
    Validates LangChain documents.
    """

    REQUIRED_METADATA = (
        "file_name",
        "file_type",
        "file_extension",
        "file_path",
        "document_type"
    )

    @classmethod
    def validate(
        cls,
        documents: list[Document]
    ) -> list[Document]:

        try:

            valid_documents = []

            for document in documents:

                cls._validate_document(document)

                valid_documents.append(document)

            return valid_documents

        except Exception as exception:

            raise PreprocessingException(
                "Failed to validate documents."
            ) from exception

    @classmethod
    def _validate_document(
        cls,
        document: Document
    ) -> None:

        if not document.page_content.strip():

            raise PreprocessingException(
                "Document content cannot be empty."
            )

        for field in cls.REQUIRED_METADATA:

            if field not in document.metadata:

                raise PreprocessingException(
                    f"Missing metadata field: {field}"
                )

            if document.metadata[field] is None:

                raise PreprocessingException(
                    f"Metadata '{field}' cannot be None."
                )