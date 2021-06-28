import pytest
import logging

@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger

    pass

@pytest.mark.usefixtures("setup1")
class BaseClass1:
    def getLogger(self):
        logger = logging.getLogger(__name__)

        fileHandler = logging.FileHandler("logfile.log")
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger
    pass