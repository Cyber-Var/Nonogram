import logging

from ui.game_window import GameWindow


class Start:

    logging.basicConfig()
    logging.root.setLevel(logging.NOTSET)
    logger = logging.getLogger("Start.class")

    def __init__(self):
        self.logger.info("Game started.")
        self.start()

    def start(self):
        window = GameWindow()

