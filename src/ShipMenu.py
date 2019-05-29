import pygame as py

class ShipMenu:
    def __init__(self, surf, board, log):
        self.__surface = surf
        self.__font = py.font.SysFont("arial", 15)
        self.__borders = [py.Rect(x, 480, 80, 30) for x in [40, 130, 220, 310]]
        self.how_many = 0
        self.__visible = True

        self.__board = board
        self.__log = log

    def draw(self):
        if self.__visible:
            for i, name in zip(self.__borders, ("x2", "x3", "x4", "x6")):
                py.draw.rect(self.__surface, (255, 255, 255), i, 1)

                rect = py.Rect(i.x + 45, i.y + 5, 20, 20)
                py.draw.rect(self.__surface, (255, 255, 255), rect)

                out = self.__font.render(name, True, (255, 255, 255))
                self.__surface.blit(out, (i.x + 20, i.y + 5))

    def on_click(self, pos):
        if self.__visible:
            i = 0
            for border in self.__borders:
                if border.collidepoint(pos[0], pos[1]):
                    if self.__board.ship_length != 0:
                        break
                    if i == 0:
                        if self.__board.number_of_ships[0] > 0:
                            self.__board.ship_length = 2
                            self.__log.print("Ship length set to 2")
                            self.__board.number_of_ships[0] -= 1
                        else:
                            self.__log.print("You have no 2 - segments ships left", (255, 0, 0))
                    elif i == 1:
                        if self.__board.number_of_ships[1] > 0:
                            self.__board.ship_length = 3
                            self.__log.print("Ship length set to 3")
                            self.__board.number_of_ships[1] -= 1
                        else:
                            self.__log.print("You have no 3 - segments ships left", (255, 0, 0))
                    elif i == 2:
                        if self.__board.number_of_ships[2] > 0:
                            self.__board.ship_length = 4
                            self.__log.print("Ship length set to 4")
                            self.__board.number_of_ships[2] -= 1
                        else:
                            self.__log.print("You have no 4 - segments ships left", (255, 0, 0))
                    elif i == 3:
                        if self.__board.number_of_ships[3] > 0:
                            self.__board.ship_length = 6
                            self.__log.print("Ship length set to 6")
                            self.__board.number_of_ships[3] -= 1
                        else:
                            self.__log.print("You have no 6 - segments ships left", (255, 0, 0))


                else:
                    i += 1

        if self.__board.number_of_ships == [0, 0, 0, 0]:
            self.__visible = False
            self.__log.print("Place last ship and battle will begin.", (0, 255, 0))

