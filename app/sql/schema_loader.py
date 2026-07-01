from sqlalchemy import inspect

from app.core.exceptions import SQLException

from app.sql.database import DatabaseConnection


class SchemaLoader:
    """
    Loads database schema from MySQL.
    """

    def __init__(self):

        self.engine = DatabaseConnection().connect()

    def load_schema(self) -> str:

        try:

            inspector = inspect(self.engine)

            schema = ""

            for table in inspector.get_table_names():

                schema += f"Table: {table}\n"

                columns = inspector.get_columns(table)

                for column in columns:

                    schema += (
                        f"{column['name']} ({column['type']})\n"
                    )

                schema += "\n"

            return schema.strip()

        except Exception as exception:

            raise SQLException(
                "Failed to load database schema."
            ) from exception