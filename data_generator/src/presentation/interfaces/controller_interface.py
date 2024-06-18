from abc import ABC, abstractmethod
from typing import Dict

class ControllerInterface(ABC):

    @abstractmethod
    def handle(self, request: Dict) -> Dict:
        pass
