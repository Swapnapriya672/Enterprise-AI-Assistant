from app.core.exceptions import PipelineException

from app.intent.intent_manager import IntentManager
from app.intent.intent_types import IntentType

from app.pipeline.query_pipeline import QueryPipeline

from app.sql.sql_manager import SQLManager


class PipelineManager:
    """
    Enterprise AI pipeline.
    """

    def __init__(self):

        self.intent_manager = IntentManager()

        self.rag_pipeline = QueryPipeline()

        self.sql_pipeline = SQLManager()

    def query(
        self,
        query: str
    ) -> dict:

        try:

            intent = self.intent_manager.classify(
                query
            )
            print("=" * 60)
            print("Query :", query)
            print("Intent:", intent)
            print("=" * 60)


            if intent == IntentType.SQL:
                print(">>> SQL Pipeline")

                return self.sql_pipeline.process(
                    query
                )
            print(">>> RAG Pipeline")
            return self.rag_pipeline.run(
                query
            )

        except Exception as exception:

            raise PipelineException(
                "Pipeline execution failed."
            ) from exception