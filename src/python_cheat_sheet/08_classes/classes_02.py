import logging

logging.basicConfig(level = logging.INFO)

class Second:
    def __init__(self, l: list):
        self.lst = l

second = Second([1, 2, 3, 4, 5])
logging.info(second.lst)
