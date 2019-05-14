from src.Utility import *

class Ship:
    def __init__(self, seg):
        self.__segments = []
        seg.is_active = True
        self.__segments.append(seg)

    def add_segment(self, seg):
        seg.is_active = True
        self.__segments.append(seg)

