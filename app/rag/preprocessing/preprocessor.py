from copy import deepcopy

from langchain_core.documents import Document

from app.core.exceptions import PreprocessingException

from app.rag.preprocessing.document_validator import (
    DocumentValidator,
)

from app.rag.preprocessing.text_cleaner import (
    TextCleaner,
)

from app.rag.preprocessing.metadata_processor import (
    MetadataProcessor,
)


class Preprocessor:
    """
    Complete preprocessing pipeline.
    """

    def process(
        self,
        documents: list[Document]
    ) -> list[Document]:

        try:

            processed_documents = deepcopy(documents)

            processed_documents = DocumentValidator.validate(
                processed_documents
            )

            for index, document in enumerate(processed_documents):

                document = TextCleaner.clean(document)

                document = MetadataProcessor.process(document)

                processed_documents[index] = document

            return processed_documents

        except Exception as exception:

            raise PreprocessingException(
                "Failed to preprocess documents."
            ) from exception