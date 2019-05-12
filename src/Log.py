import pygame as py

class LogWindow:
    def __init__(self, surface):
        self.__border = py.Rect(20, 530, 940, 150)
        self.__surf = surface
        self.__font = py.font.SysFont("arial", 15)
        self.__out = []

    def draw(self):
        py.draw.rect(self.__surf, (255, 255, 255), self.__border, 1)

        # Drawing text
        x = self.__border.x + 10
        y = self.__border.y + 10
        for i in self.__out:
            self.__surf.blit(i, (x, y))
            y += 16

    def print(self, input, color = (255, 255, 255)):
        self.__out.append(self.__font.render(input, True, color))