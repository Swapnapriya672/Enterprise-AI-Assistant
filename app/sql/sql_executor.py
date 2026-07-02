from sqlalchemy import text

from app.core.exceptions import SQLException

from app.sql.database import DatabaseConnection


class SQLExecutor:
    """
    Executes SQL query.
    """

    def __init__(self):

        self.engine = DatabaseConnection().connect()

    def execute(
        self,
        sql: str
    ) -> list[dict]:

        try:

            with self.engine.connect() as connection:

                result = connection.execute(
                    text(sql)
                )

                return [

                    dict(row._mapping)

                    for row in result

                ]

        except Exception as exception:


            print("=" * 80)
            print("SQL Execution Failed")
            print(sql)
            print(exception)
            print("=" * 80)

            raise