"""
logging.py
Reference of logging in python
"""
import logging


def init():
    return True


"""
to log an event, a severity level must be assigned
then, we can log only events of a specific severity level

DEBUG
INFO
WARNING   - default level
ERROR
CRITICAL

basicConfig(**kwargs)
level
filename
filemode
format  '%(process)d - %(name)s - %(levelname)s - %(message)s'
"""


def config():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s') # noqa
    logging.debug('this will get logged')
    logging.warning('this is a warning')


def stacktrace():
    try:
        5/0
    except Exception:
        logging.debug('Exception occurred', exc_info=True)
        logging.exception('logging.exception call')

# config()
# stacktrace()


"""
Logger
LogRecord - creates LogRecords objects
Handler - sends the LogRecord to the output destination
Formatter - specify the string format
"""


def simplelogging():
    logger = logging.getLogger(__name__)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('project.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.ERROR)


    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s') # noqa
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # noqa

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    logger.warning('This is a warning')
    logger.error('This is an error')


simplelogging()
