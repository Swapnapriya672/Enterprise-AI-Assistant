from fastapi import APIRouter

from app.api.request_models import QueryRequest
from app.api.response_models import QueryResponse

from app.pipeline.pipeline_manager import PipelineManager

router = APIRouter()

pipeline = PipelineManager()


@router.post(
    "/query",
    response_model=QueryResponse
)
def query(
    request: QueryRequest
):

    return pipeline.query(
        request.query
    )