# Import all the relevant files needed to perform basic actions
import sys
import pygame
from pygame.locals import *

# Initialize pygame files
pygame.init()

# Setting up colour variables
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
myColour = (0, 0, 0)

# Set window parameters
width = 800
height = 600

# Set the window to be the height and width.
window = pygame.display.set_mode((width, height))

# Event Loop
while True:

    # Check if the Quit event has been called.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Check for button presses then setting the appropriate colour.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                myColour = red

            if event.key == pygame.K_2:
                myColour = green

            if event.key == pygame.K_3:
                myColour = blue

    # Set the window fill and update the display.
    window.fill(myColour)
    pygame.display.update()
