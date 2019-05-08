import sys, pygame

pygame.init()

size = width, height = 620, 640
speed = [1, 1]
black = 0, 0, 0
white = 225, 225, 225

screen = pygame.display.set_mode(size)

ship_element = pygame.Rect(100, 100, 10, 10)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ship_element = ship_element.move(speed)
    if ship_element.left < 0 or ship_element.right > width:
        speed[0] = -speed[0]
    if ship_element.top < 0 or ship_element.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    pygame.draw.rect(screen, white, ship_element)
    pygame.display.flip()