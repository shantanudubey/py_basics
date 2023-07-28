# Logging

""" Levels :
        - Debug
        - Info
        - Warning
        - Error
        - Critical Error
"""

import os
import logging


print('-'*79)
# NOTSET will set it at logging level 0, DEBUG will set it to 10 and onwards in steps of 10
# Ref : https://towardsdatascience.com/how-to-setup-logging-for-your-python-notebooks-in-under-2-minutes-2a7ac88d723d
logging.getLogger().setLevel(logging.NOTSET)


logging.debug("This is a debug log for testing.")
logging.info("This is a info log for testing.")
logging.warning("This is a warning log for testing.")
logging.error("This is a error log for testing.")
logging.critical("This is a critical log for testing.")


def add(x,y):
    logging.debug(f"Parameters passed : {x} and {y}")
    return x + y

print("Logging status :", logging.getLogger().getEffectiveLevel(), logging.getLogger().isEnabledFor(logging.DEBUG))
print("Result : ", add(4, 6))
print('-'*79)

# 'r' is the "raw" character that denotes that the '\' is to be considered as a backslash and not a escape character 
DIR_PATH = os.getcwd()
LOG_FILE = "system.txt"

full_path = os.path.join(DIR_PATH, LOG_FILE)
print("Location :", full_path)

os.makedirs(DIR_PATH, exist_ok=True)
logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)
file_handler = logging.FileHandler(full_path)
file_handler.setFormatter(logging.Formatter("%(asctime)s : %(levelname)S : %(message)"))
logger.addHandler(file_handler)

def check_system(sys):
    if sys != "OK":
        logging.critical(f"System Failure : {sys}")
        
check_system("This Error should be resolved first.")
file_handler.close()


print('-'*79)