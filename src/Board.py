import pygame as py

class Board:
    """Representation of board/sea"""
    def __init__(self, x, y, surface, title):
        self.__x = x
        self.__y = y
        self.__width = 45
        self.__height = 45
        self.__surf = surface

    def draw(self):
        x = self.__x
        y = self.__y
        for i in range(10):
            for j in range(10):
                py.draw.rect(self.__surf, (255, 255, 255), (x, y, 40, 40), 1)
                x += 40
            y += 40
            x = self.__x

        font = py.font.SysFont("timesnewroman", 23)
        text_top = [font.render(x, True, (225, 225, 225)) for x in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']]
        text_side = [font.render(str(x), True, (225, 225, 225)) for x in range(10)]

        # Drawing top letter coordinates
        x = self.__x + 10
        y = self.__y - 28
        for i in text_top:
            self.__surf.blit(i, (x, y))
            x += 41

        # Drawing side number coordinates
        x = self.__x - 18
        y = self.__y + 3
        for i in text_side:
            self.__surf.blit(i, (x, y))
            y += 41
