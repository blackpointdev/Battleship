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

            # TODO Split to functions
            # 2-segments ships generation
            while True:
                for i in range(2):
                    while True:
                        pos = random.randint(0, 99)
                        if pos not in self.__board_ai.ships:
                            index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                                  self.__board_ai.ship_status, pos)
                            if index >= 0:
                                print(pos)
                                break

                    self.__board_ai.ships.append(index)
                    self.__board_ai.segments[index].status = self.__board_ai.ship_status

                    for j in range(15):
                        direction = random.randint(0, len(available) - 1)
                        print(available[direction])
                        tmp, tmp2 = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                                self.__board_ai.ship_status, direction)
                        if tmp >= 0:
                            # print(available[direction])
                            tmp, tmp2 = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                               self.__board_ai.ship_status, available[direction])
                            if tmp >= 0:
                                self.__board_ai.ships.append(available[direction])
                                self.__board_ai.segments[available[direction]].status = self.__board_ai.ship_status
                                self.__board_ai.ship_status += 1
                                self.__board_ai.number_of_ships[0] -= 1
                                break
                    else:
                        continue

                    break

                # 3-segments ships generation
                while True:
                    for i in range(2):
                        while True:
                            pos = random.randint(0, 99)
                            if pos not in self.__board_ai.ships:
                                index, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                                          self.__board_ai.ship_status, pos)
                                if index >= 0:
                                    print(pos)
                                    break

                        self.__board_ai.ships.append(index)
                        self.__board_ai.segments[index].status = self.__board_ai.ship_status

                        for j in range(2):
                            for j in range(15):
                                direction = random.randint(0, len(available) - 1)
                                print(available[direction])
                                tmp, available = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                                   self.__board_ai.ship_status, direction)
                                if tmp >= 0:
                                    # print(available[direction])
                                    tmp, tmp2 = validate_ship_position(self.__board_ai.segments, self.__board_ai.log,
                                                                       self.__board_ai.ship_status, available[direction])
                                    if tmp >= 0:
                                        self.__board_ai.ships.append(available[direction])
                                        self.__board_ai.segments[available[direction]].status = self.__board_ai.ship_status
                                        self.__board_ai.ship_status += 1
                                        self.__board_ai.number_of_ships[0] -= 1
                                        break
                            else:
                                continue

                    break
                break