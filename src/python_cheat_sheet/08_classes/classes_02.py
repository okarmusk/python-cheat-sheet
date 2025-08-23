import logging

logging.basicConfig(level = logging.INFO)

class Second:
    def __init__(self, l: list):
        self.lst = l

    def method_a(self, arg: str):
        logging.info(arg)

second = Second([1, 2, 3, 4, 5])
logging.info(second.lst)
second.method_a('Display a method_a call')
