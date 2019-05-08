import pygame as py
import sys
from src import Board

py.init()

size = width, height = 1000, 540
black = 0, 0, 0
white = 225, 225, 225

screen = py.display.set_mode(size)
board_player = Board.Board(40, 80, screen, "Player")
board_ai = Board.Board(560, 80, screen, "AI")

while 1:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()

    screen.fill(black)
    board_player.draw()
    board_ai.draw()
    py.display.flip()