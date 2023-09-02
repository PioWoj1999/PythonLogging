import logging
from logging.handlers import SysLogHandler

# URL: https://my.papertrailapp.com/events
PAPERTRAIL_HOST = "logs5.papertrailapp.com"
PAPERTRAIL_PORT = 53361


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
