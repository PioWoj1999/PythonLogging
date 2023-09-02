import logging

def main() -> None: 
    # supply basic configuration of logging - specifiers which logs are going to be displayed
    # logging. basicConfig(level=logging.WARNING)
    # logging. basicConfig(level=logging.INFO)
    logging. basicConfig(level=logging.DEBUG)

    logging.debug("This is a debug message.")
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
    logging.critical("This is a critical message.")

if __name__ == "__main__":
    main()