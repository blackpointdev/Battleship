import pygame as py
import sys
from src import Board
from src import Log
from src import ShipMenu
from src import Ai

py.init()
py.display.set_caption("Battleship - Marcin Wiśnios")
ico = py.image.load("../res/icon.png")
py.display.set_icon(ico)

size = width, height = 1000, 700
black = 0, 0, 0
white = 225, 225, 225

screen = py.display.set_mode(size)
log = Log.LogWindow(screen)

board_player = Board.Board(40, 80, screen, log, "Player")
board_ai = Board.BoardAI(560, 80, screen, log, "AI", False)
ai = Ai.AI(screen, board_ai, board_player)
ai.generate_ships()
log.clear()

log.print("Battleship v. 1.0")
log.print("Place your ships on the battlefield.", (0, 255, 0))

shipMenu = ShipMenu.ShipMenu(screen, board_player, log)

fps = 15
clock = py.time.Clock()

while 1:
    for event in py.event.get():
        # Handling close event
        if event.type == py.QUIT: sys.exit()
        # Handling click event
        if event.type == py.KEYDOWN:
            if event.key == py.K_ESCAPE:
                sys.exit()
            if event.key == py.K_v:
                board_ai.is_visible = not board_ai.is_visible
        if event.type == py.MOUSEBUTTONUP:
            pos = py.mouse.get_pos()
            if pos[0] > 40 and pos[0] < 440 and pos[1] > 80 and pos[1] < 480:
                if event.button == 3:
                     board_player.reset()
                if event.button == 1:
                    board_player.on_click(pos)
            elif pos[0] > 560 and pos[0] < 960 and pos[1] > 80 and pos[1] < 480 and board_player.is_ready:
                if board_ai.on_click(pos):
                    ai.shoot()
            else:
                shipMenu.on_click(pos)


    screen.fill(black)
    board_player.draw()
    board_ai.draw()
    log.draw()
    shipMenu.draw()
    py.display.flip()
    clock.tick(fps)
