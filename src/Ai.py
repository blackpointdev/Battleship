import pygame as py
from src.Utility import validate_ship_position
import random

class AI:
    def __init__(self, surf, board_ai, board_player):
        self.__surface = surf
        self.__board_ai = board_ai
        self.__board_player = board_player

    def generate_ships(self):
        # while self.__board_ai.number_of_ships != [0, 0, 0, 0]:

        # 2-segments ships generation
        for i in range(2):
            while True:
                pos = random.randint(0, 99)
                if pos not in self.__board_ai.ships:
                    index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                          self.__board_ai.ship_status, pos)
                    if index >= 0:
                        break

            self.__board_ai.ships.append(index)
            self.__board_ai.segments[index].status = self.__board_ai.ship_status

            for j in range(15):
                direction = random.randint(0, len(available) - 1)
                tmp, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                        self.__board_ai.ship_status, direction)
                if available != (-10, -10):
                    self.__board_ai.ships.append(available[direction])
                    self.__board_ai.segments[available[direction]].status = 1
                    self.__board_ai.ship_status += 1
                    break

            # 3-segments ships generation
            # for i in range(2):
            #     while True:
            #         pos = random.randint(0, 99)
            #         if pos not in self.__board_ai.ships:
            #             index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
            #                                                       self.__board_ai.ship_status, pos)
            #             if index >= 0:
            #                 break
            #
            #     self.__board_ai.ships.append(index)
            #     self.__board_ai.segments[index].status = self.__board_ai.ship_status
            #
            #     direction = random.randint(0, len(available) - 1)
            #     self.__board_ai.segments[available[direction]].status = 1
                # for i in range(1):
                #     index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                #                                               self.__board_ai.ship_status, pos)
                #     direction = random.randint(0, len(available) - 1)
                #     self.__board_ai.segments[available[direction]].status = 1
