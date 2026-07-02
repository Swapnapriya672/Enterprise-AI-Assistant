from abc import ABC
from abc import abstractmethod


class BaseTool(ABC):
    """
    Base class for every agent tool.
    """

    @abstractmethod
    def run(
        self,
        query: str
    ) -> dict:
        """
        Executes the tool.
        """
        pass