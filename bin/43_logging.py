"""
logging: To capture messages in log file

Levels
INFO
DEBUG
WARNING
CRITICAL
ERROR
"""

print("Logging Example:")
print("-"*20)
# -------------

import logging

my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)

log_format_we_want = logging.Formatter("%(levelname)s : %(filename)s - %(message)s")

# print to console
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(log_format_we_want)
my_logger.addHandler(consoleHandler)

# write to my log file
fileHandler = logging.FileHandler("my_logging_log.log", "a")
fileHandler.setFormatter(log_format_we_want)
my_logger.addHandler(fileHandler)

# Instead of using print() function, we can use below methods
my_logger.info("This is Info message")
my_logger.debug("This is debug message")
my_logger.warning("This is warning message")
my_logger.critical("This is critical message")
my_logger.error("This is error message")

print("#"*40, end="\n\n")
#########################