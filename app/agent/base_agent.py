from abc import ABC
from abc import abstractmethod


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    @abstractmethod
    def plan(
        self,
        query: str
    ) -> list[str]:
        """
        Plans which tools should execute.
        """
        pass