import logging

def test_loggingwazo():
    logger = logging.getlogger(__name__)



    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s") # time displayed
    fileHandler.setFormatter(formatter)



    logger.addHandler() #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A major error has happened")
    logger.critical("Critical issue")


