import sys
import pygame
from pygame.locals import *

pygame.init()

width = 800
height = 600

clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode((width, height))

player = pygame.image.load('Images/flatbrick.gif')
playerX = 400
playerY = 550

white = (255, 255, 255)

while True:
    keysPressed = pygame.key.get_pressed()

    window.fill(white)
    window.blit(player, (playerX, playerY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    if keysPressed[K_RIGHT]:
        playerX += 10

    if keysPressed[K_LEFT]:
        playerX -= 10

    pygame.display.update()
    clock.tick(fps)
