from app.agent.base_agent import BaseAgent

from app.agent.planner_prompt import PlannerPrompt

from app.agent.planner_parser import PlannerParser

from app.llm.llm_manager import LLMManager

from app.core.exceptions import PipelineException


class Planner(BaseAgent):
    """
    Enterprise AI Planner.
    """

    def __init__(self):

        self.llm = LLMManager()

    def plan(
        self,
        query: str
    ) -> list[str]:

        try:

            prompt = PlannerPrompt.build(
                query=query
            )

            response = self.llm.generate(
                prompt
            )

            return PlannerParser.parse(
                response
            )

        except Exception as exception:

            raise PipelineException(
                "Planning failed."
            ) from exception