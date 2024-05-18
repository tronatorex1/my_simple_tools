# This is an example on how to use AutoPyLogger which seems to be easier than Python's Logger
#    It has box log rotation and critical logs mailing facility built

# import the package
from autopylogger import init_logging

# Initialise the logging module

format = '[%(asctime)s] : %(levelname)s - %(filename)s / %(funcName)s [ Line_no: %(lineno)d ] = %(message)s'
mylogger = init_logging(log_name="MyLogsFolders", log_directory="c:/ALEX", log_format=format) # within a unique folder per status will be created as well as the log file related to the status

def pseudo_main():
    # Write logs - DEBUG | INFO | WARNING | ERROR
    mylogger.debug('This is a INFO log')
    mylogger.info('This is a DEBUG log')
    mylogger.warning('This is a WARNING log')
    mylogger.error('This is a ERROR log')

pseudo_main()