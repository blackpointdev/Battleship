from src.Utility import create_ship
from src.Utility import check_positions
import random


class AI:
    def __init__(self, surf, board_ai, board_player):
        self.__surface = surf
        self.__board_ai = board_ai
        self.__board_player = board_player
        self.__shot = [x for x in range(100)]
        self.__available = []
        self.__game_over = False

    def generate_ships(self):
        # 2-segments ships generation
        create_ship(self.__board_ai, 2, 2)

        # 3-segments ships generation
        create_ship(self.__board_ai, 3, 2)

        # 4-segments ships generation
        create_ship(self.__board_ai, 4, 2)

        # 6-segments ships generation
        create_ship(self.__board_ai, 6, 1)


    def shoot(self):
        if not self.__game_over:
            status = -1
            # Fair play (computer chooses random coordinates)
            # target = random.choice(self.__shot)
            # godlike (computer always hits one of players' ships
            target = random.choice(self.__board_player.ships)

            if self.__board_player.segments[target].status > 1:
                i = 0
                for segment in self.__board_player.segments:
                    if segment.status == self.__board_player.segments[target].status:
                        self.__available.append(i)
                    i += 1
                status = self.__board_player.segments[target].status
                self.__board_player.segments[target].status = 0
                self.__board_player.ships.remove(target)

                print(self.__available)

            else:
                self.__board_player.segments[target].status = 1

            self.__shot.remove(target)

            for segment in self.__board_player.segments:
                if segment.status == status:
                    break
            else:
                self.__board_player.log.print("Your ship has been destroyed!", (255, 140, 0))
                if len(self.__board_player.ships) == 0:
                    self.__board_player.log.print("AI WINS!", (0, 255, 0))
                    self.__game_over = True
                    self.__board_ai.game_over = True