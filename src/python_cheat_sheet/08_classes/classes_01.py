import logging

logging.basicConfig(level = logging.INFO)

class First:
    variable = 32

    def method_a(self):
        logging.info("method_a")

first = First()
first.method_a()
logging.info(first.variable)

# Class specific fields
first.specific_field = "Specific field."
logging.info(first.specific_field)
another_first = First()

try :
    # specific_field is unknown field, throw AttributeError
    logging.info(another_first.specific_field)
except AttributeError:
    pass
