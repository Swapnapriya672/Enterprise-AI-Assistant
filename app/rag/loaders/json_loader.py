import json

from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class JSONLoader(BaseLoader):
    """
    Loader for JSON documents.
    """

    def load(self) -> list[Document]:

        json_documents = []

        try:

            json_files = self.documents_path.glob("*.json")

            for json_file in json_files:

                with open(
                    json_file,
                    mode="r",
                    encoding="utf-8"
                ) as file:

                    json_data = json.load(file)

                metadata = self.create_metadata(
                    file_path=json_file,
                    document_type="JSON Document"
                )

                metadata.update(
                    {
                        "total_keys": (
                            len(json_data)
                            if isinstance(json_data, dict)
                            else None
                        )
                    }
                )

                document = Document(
                    page_content=json.dumps(
                        json_data,
                        indent=4,
                        ensure_ascii=False
                    ),
                    metadata=metadata
                )

                json_documents.append(document)

            return json_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load JSON documents."
            ) from exception