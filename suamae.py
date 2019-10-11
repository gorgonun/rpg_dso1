from controllers.historyController import HistoryController
import logging

if __name__ == "__main__":
    log = logging.getLogger("log")
    log.addHandler(logging.FileHandler("log.log", "a"))
    log.setLevel(logging.DEBUG)

    history = HistoryController(log)

    while True:
        log.info("Starting game")
        result = history.start_game()
        if result != 1:
            log.info("Exiting")
            exit()
