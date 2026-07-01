from app.core.exceptions import SQLException

from app.sql.schema_loader import SchemaLoader

from app.sql.sql_generator import SQLGenerator

from app.sql.sql_validator import SQLValidator

from app.sql.sql_executor import SQLExecutor

from app.sql.response_formatter import (
    SQLResponseFormatter,
)


class SQLManager:
    """
    Main SQL pipeline.
    """

    def __init__(self):

        self.schema_loader = SchemaLoader()

        self.generator = SQLGenerator()

        self.validator = SQLValidator()

        self.executor = SQLExecutor()

    def process(
        self,
        query: str
    ) -> dict:

        try:
            
            print("SQL Manager Started")

            schema = self.schema_loader.load_schema()
            print(schema)

            sql = self.generator.generate_sql(
                query=query,
            
                schema=schema
            )

            sql = self.validator.validate(
                sql
            )

            rows = self.executor.execute(
                sql
            )

            return SQLResponseFormatter.format(
                rows
            )

        except Exception as exception:

            print("=" * 80)
            print("Original Exception")
            print(repr(exception))
            print("=" * 80)

            raise