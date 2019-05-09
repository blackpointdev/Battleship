import pygame as py
import sys
from src import Board

py.init()
py.display.set_caption("Battleship - Marcin Wiśnios")
ico = py.image.load("../res/icon.png")
py.display.set_icon(ico)

size = width, height = 1000, 540
black = 0, 0, 0
white = 225, 225, 225

screen = py.display.set_mode(size)
board_player = Board.Board(40, 80, screen, "Player")
board_ai = Board.Board(560, 80, screen, "AI")

tmp_mouse = (0, 0)

while 1:
    for event in py.event.get():
        if event.type == py.QUIT: sys.exit()

    screen.fill(black)
    board_player.draw()
    board_ai.draw()
    py.display.flip()

    mouse_pos = py.mouse.get_pos()
    if mouse_pos != tmp_mouse:
        print(py.mouse.get_pos())
        tmp_mouse = mouse_pos