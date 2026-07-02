from app.core.exceptions import PipelineException


class PlannerParser:
    """
    Parses planner output.
    """

    @staticmethod
    def parse(
        response: str
    ) -> list[str]:

        try:

            response = response.strip()

            if response == "NONE":

                return []

            tools = [

                tool.strip()

                for tool

                in response.split(",")

            ]

            return tools

        except Exception as exception:

            raise PipelineException(
                "Failed to parse planner response."
            ) from exception