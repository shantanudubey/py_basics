import logging
import sys

print('-'*79)

LOG_FILE = "logs/errors.log"
fs_date = '%d/%m/%Y %I:%M:%S %p'
fs_log = '%(asctime)s : %(levelname)-8s : %(name)s : %(message)s'
# Changing default formatter
log_formatter = logging.Formatter(fs_log, datefmt=fs_date)
root_logger = logging.getLogger()

# Don't initialize the default logger to avoid duplicate logging
#  when events get propagated

# stdout : 
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_formatter)
console_handler.set_name(__name__+".console")
root_logger.addHandler(console_handler)
# log-file
file_handler = logging.FileHandler(LOG_FILE, "a")
file_handler.setFormatter(log_formatter)
file_handler.set_name(__name__+".file")
root_logger.addHandler(file_handler)

try:
    #res = 456 / 0
    lst = []
    lst[2]    
    
except ZeroDivisionError as e:
    logging.error("Cannot divide by zero : "+ str(e))
except Exception as e:
    logging.error("Some error occured : " + str(e))


# Cleanup : Should be done by the main-app before exiting
root_logger.removeHandler(file_handler)
root_logger.removeHandler(console_handler)
file_handler.close()
console_handler.close()

# This will be logged by the default handler since we've removed
#    our custom handlers
logging.error("Test Error  after removing custom handlers.")

print('-'*79)