from abc import ABC, abstractmethod


class BaseSQL(ABC):
    """
    Base class for SQL generation.
    """

    @abstractmethod
    def generate_sql(
        self,
        query: str,
        schema: str
    ) -> str:
        """
        Generate SQL query.
        """
        pass