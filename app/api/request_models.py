from pydantic import BaseModel


class QueryRequest(BaseModel):
    """
    Request model.
    """

    query: str