from app.tools.base_tool import BaseTool

from app.sql.sql_manager import SQLManager

from app.core.exceptions import SQLException


class SQLTool(BaseTool):
    """
    Tool for executing SQL queries.
    """

    def __init__(self):

        self.pipeline = SQLManager()

    def run(
        self,
        query: str
    ) -> dict:

        try:

            return self.pipeline.process(
                query=query
            )

        except Exception as exception:

            print("=" * 80)
            print("SQL Tool Failed")
            print(type(exception))
            print(repr(exception))
            print("=" * 80)

            raise