import pandas as pd

from langchain_core.documents import Document

from app.core.exceptions import DocumentLoaderException
from app.rag.loaders.base_loader import BaseLoader


class ExcelLoader(BaseLoader):
    """
    Loader for Microsoft Excel documents.
    """

    def load(self) -> list[Document]:

        excel_documents = []

        try:

            excel_files = self.documents_path.glob("*.xlsx")

            for excel_file in excel_files:

                excel_data = pd.read_excel(
                    excel_file,
                    sheet_name=None
                )

                for sheet_name, dataframe in excel_data.items():

                    metadata = self.create_metadata(
                        file_path=excel_file,
                        document_type="Excel Document"
                    )

                    metadata.update(
                        {
                            "sheet_name": sheet_name,
                            "rows": len(dataframe),
                            "columns": list(dataframe.columns)
                        }
                    )

                    document = Document(
                        page_content=dataframe.to_csv(index=False),
                        metadata=metadata
                    )

                    excel_documents.append(document)

            return excel_documents

        except Exception as exception:

            raise DocumentLoaderException(
                "Failed to load Excel documents."
            ) from exception