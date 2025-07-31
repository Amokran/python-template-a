from pyzkolari import LogManager as log

LOG_PATH = "logs"

def main():

    # Initialize the log manager
    LOGGER = log.LogManager(brieffilename= "example", logfolder = LOG_PATH)
    LOGGER.info("LogManager initialized successfully.")

    print("Hello, World!")  

    LOGGER.info("Main function executed successfully.")


if __name__ == "__main__":
    main()