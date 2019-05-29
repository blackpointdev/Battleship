from src.Utility import create_ship
from src.Utility import spotted_shot
import random


class AI:
    def __init__(self, surf, board_ai, board_player):
        self.__surface = surf
        self.__board_ai = board_ai
        self.__board_player = board_player
        self.__shot = [x for x in range(100)]
        self.__available = []
        self.__first_available = []
        self.__game_over = False
        self.__first_shot = -1
        self.__bias = -100

    def reboot(self):
        self.__init__(self.__surface, self.__board_ai, self.__board_player)

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
            target = 0
            # Fair play (computer chooses random coordinates)
            if len(self.__available) == 0:
                target = random.choice(self.__shot)
            else:
                target = random.choice(self.__available)

            # godlike (computer always hits one of players' ships
            # target = random.choice(self.__board_player.ships)

            if self.__board_player.segments[target].status > 1:
                if self.__first_shot < 0:
                    self.__available = spotted_shot(target)
                    self.__first_available = self.__available.copy()
                    self.__first_shot = target
                else:
                    self.__available.clear()
                    if self.__bias == -100:
                        self.__first_available.remove(target)
                        self.__bias = (target - self.__first_shot)

                    if self.__bias + target in spotted_shot(target):
                        self.__available.append(self.__bias + target)
                    else:
                        self.__available.clear()
                        self.__bias = -self.__bias
                        self.__available.append(self.__first_shot + self.__bias)

                status = self.__board_player.segments[target].status

                self.__board_player.segments[target].status = 0
                self.__board_player.ships.remove(target)

                print(self.__available)

            else:
                self.__board_player.segments[target].status = 1
                if len(self.__available) == 1:
                    self.__available.clear()
                    self.__available.append(self.__first_shot - self.__bias)

            if target in self.__shot:
                self.__shot.remove(target)
            if target in self.__available:
                self.__available.remove(target)

            for segment in self.__board_player.segments:
                if segment.status == status:
                    break
            else:
                self.__board_player.log.print("Your ship has been destroyed!", (255, 140, 0))
                self.__available.clear()
                self.__first_shot = -100
                self.__bias = -100
                self.__first_available.clear()
                if len(self.__board_player.ships) == 0:
                    self.__board_player.log.print("AI WINS!", (0, 255, 0))
                    self.__game_over = True
                    self.__board_ai.game_over = True