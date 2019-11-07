from controllers.historyController import HistoryController
import sys
import logging

if __name__ == "__main__":
    log = logging.getLogger("log")
    log.addHandler(logging.FileHandler("log.log", "a"))
    log.setLevel(logging.DEBUG)

    history = HistoryController(log)

    if len(sys.argv) == 2 and sys.argv[1] == "test":
        history.test_mode()

    while True:
        log.info("Starting game")

        try:
            result = history.start_game()

        except KeyboardInterrupt:
            log.info("User canceled operation")
            result = -1

        except Exception as e:
            log.info("Got unexpected exception: %s. Could not recover.", e)
            result = 1
            raise

        if result == 0:
            break
