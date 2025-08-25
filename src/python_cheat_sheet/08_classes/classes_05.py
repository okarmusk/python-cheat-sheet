import logging

logging.basicConfig(level = logging.INFO)

# Example of class with private fields
class Sixth:
    __private_shared_variable: int = 128

    def __init__(self):
        self.__private_variable_0: int = 64
        self.__private_variable_1: str = 'Another variable'

    def get_private_variable_0(self) -> int:
        return self.__private_variable_0

sixth: Sixth = Sixth()
logging.info(sixth.get_private_variable_0())


# Dataclasses
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

