import pygame as py
from src.Utility import validate_ship_position
from src.Utility import create_ship

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

