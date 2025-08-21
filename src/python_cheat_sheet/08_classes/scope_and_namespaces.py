import logging

logging.basicConfig(level = logging.INFO)

def scope():
    def local():
        variable = 32

    def non_local():
        nonlocal variable
        variable = 64

    def glob():
        global variable
        variable = 1024

    variable = 256
    local()
    logging.info(f'local() variable value: %s', variable)
    non_local()
    logging.info(f'non_local() variable value: %s', variable)
    glob()
    logging.info(f'glob() variable value: %s', variable)

scope()
logging.info(f'scope() variable value: %s', variable)
