import logging

logging.basicConfig(level = logging.INFO)

# Exception handling
try:
    invalid_operation = 1/0
except ZeroDivisionError as err:
    logging.error("Division by 0")

try:
    valid_operation = 1/2
except (ZeroDivisionError, ValueError): # More than one exception type
    pass # Do nothing
else:
    logging.info("Operation done.")


# Raising exception
try:
    error = RuntimeError("Something went totally wrong.")
    error.add_note("Note added.")
    raise error
except RuntimeError as err:
    logging.error("Catch exception with message: %s", err)
else: # Completely not necessary
    pass
finally:
    logging.info("Always executed finally block.")
