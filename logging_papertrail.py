import logging
import os
from dotenv import load_dotenv 
from logging.handlers import SysLogHandler

# URL: https://my.papertrailapp.com/events
load_dotenv()
PAPERTRAIL_HOST = os.getenv("PAPERTRAIL_HOST") or ""
PAPERTRAIL_PORT = os.getenv("PAPERTRAIL_PORT") or ""


def main() -> None:
    # create logger object that is from some part of system
    logger = logging.getLogger("Logs_from_system_1")
    logger.setLevel(level=logging.DEBUG)

    # to send logs to other service
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    # send the debug message to logger service
    logger.debug("This is a debug message.")


if __name__ == "__main__":
    main()
