# Import files for use in program
import sys
import pygame
from pygame.locals import *

# initialize pygame
pygame.init()

# Set the width and height for the screen.
width = 800
height = 600

# Set an FPS clock
clock = pygame.time.Clock()
fps = 60

# Create the window at the correct size.
window = pygame.display.set_mode((width, height))

# Set player variables and load it's image.
player = pygame.image.load('Images/flatbrick.gif')
playerX = 400
playerY = 550

# Create white
white = (255, 255, 255)

# Event Loop
while True:
    # Create an array of button presses
    keysPressed = pygame.key.get_pressed()

    # Draw things onto the screen in order of back to front
    window.fill(white)
    window.blit(player, (playerX, playerY))

    # Listen for the Quit events then close the program if true
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    # Control the player here, this program simply moves the player left and right.
    if keysPressed[K_RIGHT]:
        playerX += 10

    if keysPressed[K_LEFT]:
        playerX -= 10

    pygame.display.update()
    clock.tick(fps)
