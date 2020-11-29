import os

import logging

from utility import *


class Logger:

    # noinspection PyArgumentList
    def __init__(self, log_type="console"):
        if log_type == "console":
            logging.basicConfig(level=logging.NOTSET,
                                format='%(asctime)s %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S')
        elif log_type == "file":
            if not os.path.exists('./log'):
                os.mkdir('./log')
            file_name = './log/%s.log' % str(current_date)
            file_handler = logging.FileHandler(file_name)
            logging.basicConfig(level=logging.NOTSET,
                                format='%(asctime)s %(levelname)s %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S',
                                handlers=[file_handler])

    def getLogger(self):
        return logging.getLogger()


if __name__ == "__main__":
    logger = Logger().getLogger()
    logger.debug('print by debug')
    logger.info('print by info')
    logger.warning('print by warning')
