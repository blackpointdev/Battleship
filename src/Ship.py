# Currently unused but left for possible refactoring

from src.Utility import *

class Ship:
    id = 1
    def __init__(self, seg):
        self.__segments = []
        self.id = 1
        self.length = 0
        id += 1
        self.__segments.append(seg)

    def add_segment(self, seg):
        seg.status = self.id
        self.__segments.append(seg)

