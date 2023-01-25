import logging, os

def main():
    logging.basicConfig(level=logging.DEBUG, 
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="logs.log", filemode="a")

    user = os.getlogin()
    try:
        div = 2 / 0
    except:
        logging.exception("division by 0")

    logging.error(f"LOG ERROR {user} triggered")
    logging.debug("LOG DEBUG")
    logging.info("LOG INFO")
    logging.warning("LOG WARNING")
    logging.error("LOG ERROR")
    logging.critical("LOG CRITICAL")


if __name__ == '__main__':
    main()
