import pygame as py

class ShipMenu:
    def __init__(self, surf, ship_length):
        self.__surface = surf
        self.__font = py.font.SysFont("arial", 15)
        self.__borders = [py.Rect(x, 480, 80, 30) for x in [40, 130, 220]]

    def draw(self):
        for i in self.__borders:
            py.draw.rect(self.__surface, (255, 255, 255), i, 1)
            out = self.__font.render("x2", True, (255, 255, 255))
            self.__surface.blit(out, (i.x + 5, i.y + 5))

    def on_click(self, pos):
        i = 0
        for border in self.__borders:
            if border.collidepoint(pos[0], pos[1]):
                if i == 0:

                i += 1
