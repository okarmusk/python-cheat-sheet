import logging

logging.basicConfig(level = logging.INFO)

class Third:
    variable = 'Third class shared variable' # CLass shared variable, till override via instance

    def __init__(self):
        logging.info('Third class constructor call')

    # class method setter
    @classmethod
    def set_variable(cls, value):
        cls.variable = value

t0 = Third()
logging.info(t0.variable)
t1 = Third()
t1.variable = 'Changed Third class shared variable'
logging.info(t0.variable) # 'Third class shared variable'
logging.info(t1.variable) # Display 'Changed Third class shared variable'
# To change it for whole class access via class
Third.variable = 'Changed Third class shared variable'
logging.info(t0.variable) # New variable value visible

Third.set_variable('Changed again Third class shared variable')
logging.info(t0.variable) # New variable value visible
