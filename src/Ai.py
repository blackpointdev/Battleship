from src.Utility import create_ship
import random


class AI:
    def __init__(self, surf, board_ai, board_player):
        self.__surface = surf
        self.__board_ai = board_ai
        self.__board_player = board_player

    def generate_ships(self):
        # TODO Split to functions
        # 2-segments ships generation
        create_ship(self.__board_ai, 2, 2)

        # 3-segments ships generation
        create_ship(self.__board_ai, 3, 2)

        # 4-segments ships generation
        create_ship(self.__board_ai, 4, 2)

        # 6-segments ships generation
        create_ship(self.__board_ai, 6, 1)

    def shoot(self):
        target = random.randint(0, 99)
        if self.__board_player.segments[target].status > 2:
            self.__board_player.segments[target].status = 0
            self.__board_player.ships.remove(target)
        else:
            self.__board_player.segments[target].status = 1