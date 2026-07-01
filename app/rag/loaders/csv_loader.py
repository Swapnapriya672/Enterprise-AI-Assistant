import pandas as pd

from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class CSVLoader(BaseLoader):
    """
    Loader for CSV documents.
    """

    def load(self) -> list[Document]:

        csv_documents = []

        try:

            csv_files = self.documents_path.glob("*.csv")

            for csv_file in csv_files:

                dataframe = pd.read_csv(csv_file)

                metadata = self.create_metadata(
                    file_path=csv_file,
                    document_type="CSV Document"
                )

                metadata.update(
                    {
                        "rows": len(dataframe),
                        "columns": list(dataframe.columns)
                    }
                )

                document = Document(
                    page_content=dataframe.to_csv(index=False),
                    metadata=metadata
                )

                csv_documents.append(document)

            return csv_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load CSV documents."
            ) from exception