from app.core.exceptions import PipelineException

from app.rag.retriever.retriever_manager import RetrieverManager
from app.rag.prompts.prompt_manager import PromptManager

from app.llm.llm_manager import LLMManager

from app.response.response_manager import ResponseManager


class QueryPipeline:
    """
    Complete query pipeline.
    """

    def __init__(self):

        self.retriever = RetrieverManager()

        self.prompt_manager = PromptManager()

        self.llm = LLMManager()

        self.response_manager = ResponseManager()

    def run(
        self,
        query: str
    ) -> dict:

        try:

            documents = self.retriever.retrieve(
                query=query
            )

            prompt = self.prompt_manager.process(
                query=query,
                documents=documents
            )

            answer = self.llm.generate(
                prompt
            )

            response = self.response_manager.process(
                answer=answer,
                documents=documents
            )

            return response

        except Exception as exception:

            raise PipelineException(
                "Query pipeline failed."
            ) from exception