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

fps = 15
clock = py.time.Clock()

while 1:
    for event in py.event.get():
        # Handling close event
        if event.type == py.QUIT: sys.exit()
        # Handling click event
        if event.type == py.MOUSEBUTTONUP:
            board_player.on_click(py.mouse.get_pos())

    screen.fill(black)
    board_player.draw()
    board_ai.draw()
    py.display.flip()
    clock.tick(fps)
