# Ref : https://docs.python.org/3/howto/logging.html

import os
import logging


print('-'*79)

# Using a formatter string with time
lf_timed = '%(asctime)s : %(levelname)-8s : %(name)s : %(message)s'
logging.basicConfig(level=logging.DEBUG, format=lf_timed, datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug("This is a debug log for testing.")
logging.info("This is a info log for testing.")
logging.warning("This is a warning log for testing.")
logging.error("This is a error log for testing.")
logging.critical("This is a critical log for testing.")
print('-'*79)


def add(x,y):
    logging.debug(f"Parameters passed : {x} and {y}")
    return x + y

print("Logging status   :", logging.getLogger().getEffectiveLevel(), logging.getLogger().isEnabledFor(logging.DEBUG))
print("Logging status   :", logging.getLogger().getEffectiveLevel(), logging.getLogger().isEnabledFor(logging.DEBUG))
print("Result           :", add(4, 6))
print('-'*79)


# Logging to a local file
DIR_PATH = os.getcwd() + r"\logs"
LOG_FILE = "system.log"

full_path = os.path.join(DIR_PATH, LOG_FILE)
print("Log file location:", full_path)

# Create folders if missing
os.makedirs(DIR_PATH, exist_ok=True)

root_logger = logging.getLogger()
root_logger.setLevel(logging.CRITICAL)
file_handler = logging.FileHandler(full_path)
file_handler.setFormatter(logging.Formatter(lf_timed))
root_logger.addHandler(file_handler)

def check_system(sys):
    if sys != "ok":
        logging.critical(f"System Failure : {sys}")
        
check_system("This Error should be resolved first.")
file_handler.close()

print('-'*79)
