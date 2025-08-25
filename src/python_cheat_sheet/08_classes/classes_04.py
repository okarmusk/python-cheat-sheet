import logging

logging.basicConfig(level = logging.INFO)

class Fourth:
    def __init__(self):
        logging.info('Fourth class constructor call')

    def method_a(self) -> int:
        return 8

    def method_b(self) -> int:
        return self.method_a()

fourth = Fourth()
logging.info(fourth.method_a())


# Inheritance
from classes_03 import Third

# Inheritance of class from another module is made by using: module_name.class_name
class Fifth(Fourth, Third):
    def __init__(self):
        super().__init__()
        logging.info('Fifth class constructor call')

fifth = Fifth()
