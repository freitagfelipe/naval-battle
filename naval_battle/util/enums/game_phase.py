from enum import Enum


class GamePhase(Enum):
    GREETINGS = 1
    READ_NAMES = 2
    READ_SHIPS = 3
    BEFORE_PLAY = 4
    PLAYING = 5
    AFTER_PLAY = 6
    PLAY_AGAIN = 7
