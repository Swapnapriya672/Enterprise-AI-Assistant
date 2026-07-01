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
                print("=" * 80)
                print("Executing SQL")
                print(sql)
                print("=" * 80)

                result = connection.execute(
                    text(sql)
                )

                return [

                    dict(row._mapping)

                    for row in result

                ]

        except Exception as exception:

            raise SQLException(
                "Failed to execute SQL."
            ) from exception