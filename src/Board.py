import pygame as py
from src import Ship
from src.Exceptions import IncorrectShipPlacement
from src.Utility import validate_ship_position

class BoardSegment:
    def __init__(self, x, y, surface):
        self.__rect = py.Rect(x, y, 40, 40)
        self.__surf = surface
        self.__ships = []
        self.is_active = False

    def draw(self):
        py.draw.rect(self.__surf, (255, 255, 255), self.__rect, 1)
        if self.is_active:
            py.draw.rect(self.__surf, (255, 0, 0), (self.__rect.x + 10, self.__rect.y + 10, 20, 20))

    def get_rect(self):
        return self.__rect


class Board:
    """Representation of board/sea"""
    def __init__(self, x, y, surface, log, title):
        self.__x = x
        self.__y = y
        self.__surf = surface
        self.__segments = []
        self.__log = log
        self.__font = py.font.SysFont("timesnewroman", 23)
        self.__ship_length = 0

        # Generating board
        x = self.__x
        y = self.__y
        for i in range(10):
            for j in range(10):
                seg = BoardSegment(x, y, self.__surf)
                # Ex. segment B1 has index 11
                # TODO Maybe find simpler solution?
                self.__segments.append(seg)
                x += 39
            y += 39
            x = self.__x

    def on_click(self, pos):
        validate_ship_position(self.__segments, pos, self.__log)


        # ----------------- Testing code -----------------
        # for segment in self.__segments:
        #     if segment.get_rect().collidepoint(pos[0], pos[1]):
        #         if not segment.is_active:
        #             segment.is_active = True
        #         else:
        #             segment.is_active = False

    def draw(self):
        for i in self.__segments:
            i.draw()

        text_top = [self.__font.render(x, True, (225, 225, 225)) for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']]
        text_side = [self.__font.render(str(x), True, (225, 225, 225)) for x in range(10)]

        # Drawing top letter coordinates
        x = self.__x + 10
        y = self.__y - 28
        for i in text_top:
            self.__surf.blit(i, (x, y))
            x += 40

        # Drawing side number coordinates
        x = self.__x - 18
        y = self.__y + 4
        for i in text_side:
            self.__surf.blit(i, (x, y))
            y += 39
