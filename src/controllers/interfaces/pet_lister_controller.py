from typing import Dict
from abc import ABC, abstractmethod

class PetListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
