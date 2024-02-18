import coloredlogs
import logging
import sys


def configure_colored_logging():
    """
    Configures colored logging with desired format and date format.

    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    """

    coloredlogs.install(level=logging.DEBUG, isatty=True,
                        fmt="%(asctime)s %(levelname)-8s %(message)s",
                        stream=sys.stdout,
                        datefmt='%Y-%m-%d %H:%M:%S')

