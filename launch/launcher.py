from launch.start import Start
import logging

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logger = logging.getLogger("Launch.file")


def main():
    try:
        start = Start()
    except:
        logger.error("*** An error occurred. ***")


if __name__ == "__main__":
    main()
