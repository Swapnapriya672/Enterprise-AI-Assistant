from pydantic import BaseModel


class Citation(BaseModel):
    file_name: str | None = None
    file_type: str | None = None
    source: str | None = None


class QueryResponse(BaseModel):

    status: str

    answer: str | None = None

    total_documents: int | None = None

    citations: list[Citation] | None = None

    total_rows: int | None = None

    data: list[dict] | None = None