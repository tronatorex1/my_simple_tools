# This example use Loguru as an alternative to python's native log framework or solution
#    

# base example with all statuses
from loguru import logger
def other_than_main():
    logger.debug("Happy logging with Loguru!")
    logger.trace("Trace......") # trace is replaced by debug as the most basic logging level
    logger.critical("Critical......")
    logger.error("Error.......")
    logger.info("Information.....")
    logger.warning("Warning........")
    logger.success("SUCCESS!!!!!!!!!!!!!!!!")

## calling pseudo main function above!
other_than_main()


# Adding more states
import sys
from loguru import logger
logger.level("FATAL", no=60, color="<red>", icon="--------")
logger.log("FATAL", "A user updated some information.")


# Formatting the stdout of logger
from loguru import logger
logger.remove(0)
logger.add(sys.stderr, format="{time} ::: {level} ::: {message}")
logger.debug("Happy logging with Loguru!")
logger.error("Happy logging with Loguru!")






