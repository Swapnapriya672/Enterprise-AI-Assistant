from app.tools.base_tool import BaseTool

from app.pipeline.query_pipeline import QueryPipeline

from app.core.exceptions import PipelineException


class RAGTool(BaseTool):
    """
    Tool for enterprise document retrieval.
    """

    def __init__(self):

        self.pipeline = QueryPipeline()

    def run(
        self,
        query: str
    ) -> dict:

        try:

            return self.pipeline.run(
                query=query
            )

        except Exception as exception:

            raise PipelineException(
                "RAG Tool execution failed."
            ) from exception