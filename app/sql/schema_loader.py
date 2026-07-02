from sqlalchemy import inspect

from app.core.exceptions import SQLException

from app.sql.database import DatabaseConnection


class SchemaLoader:
    """
    Loads and caches database schema.
    """

    _schema = None

    def __init__(self):

        self.engine = DatabaseConnection().connect()

    def load_schema(
        self
    ) -> str:

        try:

            # Return cached schema
            if SchemaLoader._schema is not None:

                return SchemaLoader._schema

            inspector = inspect(
                self.engine
            )

            schema = ""

            for table in inspector.get_table_names():

                schema += f"Table: {table}\n"

                columns = inspector.get_columns(
                    table
                )

                for column in columns:

                    schema += (
                        f"{column['name']} ({column['type']})\n"
                    )

                schema += "\n"

            SchemaLoader._schema = schema.strip()

            return SchemaLoader._schema

        except Exception as exception:

            raise SQLException(
                "Failed to load database schema."
            ) from exception

        if SchemaLoader._schema is not None:

            print("Using Cached Schema")

            return SchemaLoader._schema

            print("Loading Schema From Database")

        @classmethod
        def refresh_cache(
            cls
        ) -> None:

            cls._schema = None