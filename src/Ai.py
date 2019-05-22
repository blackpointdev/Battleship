import pygame as py
from src.Utility import validate_ship_position
import random

class AI:
    def __init__(self, surf, board_ai, board_player):
        self.__surface = surf
        self.__board_ai = board_ai
        self.__board_player = board_player

    def generate_ships(self):
        while self.__board_ai.number_of_ships != [0, 0, 0, 0]:
            while True:
                pos = random.randint(0, 99)
                if pos not in self.__board_ai.ships:
                    index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                          self.__board_ai.ship_status, pos)
                    if index >= 0:
                        break
            break
        self.__board_ai.segments[index].status = self.__board_ai.ship_status
        direction = random.randint(0, len(available) - 1)

        self.__board_ai.segments[available[direction]].status = 1
