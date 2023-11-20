from abc import ABC,abstractmethod
from random import randint
from datetime import datetime

# Pattern: Strategy Pattern
class EngineBehavior(ABC):
    @abstractmethod
    def engine_info(self):
        pass

class TurbochargerBehavior(ABC):
    @abstractmethod
    def turbocharger_info(self):
        pass
