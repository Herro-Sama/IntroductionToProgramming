import sys
import pygame
import random
from pygame.locals import *


# Declare a class this will be used in the event we wanted to have multiple balls on screen.
class Ball(pygame.sprite.Sprite):
    # This is the function called whenever you want to create a new ball.
    # It is used to store all variable in memory for use later.
    def __init__(self, spawnX, spawnY):

        # Here we are initializing this new ball as a Pygame sprite
        pygame.sprite.Sprite.__init__(self)

        # set the spawn position for the ball
        self.pos_x = spawnX
        self.pos_y = spawnY

        # Load the image the ball will be using
        self.image = pygame.image.load('Images/ball.png')

        # Choose a random speed for the ball to have when it spawns.
        self.speed_x = random.randrange(-10, 10)
        self.speed_y = random.randrange(-10, -1)

        # This is the collision rectangle which will be set to the size and position of the image.
        self.rect = self.image.get_rect()

        # Prevent ball from being spawned as stationary
        if self.speed_x == 0:
            self.speed_x = random.randrange(-10, 10)
        if self.speed_y == 0:
            self.speed_y = random.randrange(-10, 10)

    # Draw the image on the screen also a debug representation of the collider.
    def draw(self):
        window.blit(self.image, (self.pos_x, self.pos_y))
        pygame.draw.rect(window, blue, self.rect, 2)

    # Update the balls position and delete it if it goes off the bottom of the screen.
    def update(self, player):
        self.pos_x += self.speed_x
        self.pos_y += self.speed_y
        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

        if self.pos_x < 0:
            self.speed_x *= -1
        if self.pos_x > width:
            self.speed_x *= -1

        if self.pos_y < 0:
            self.speed_y *= -1
        if self.pos_y > height:
            player.ball_list.remove(self)
            self.kill()

# This is the players paddle class which is used to control the paddle at the bottom.
class Paddle(pygame.sprite.Sprite):
    # This is the paddle which will be the players character effectively.
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        # set paddle location on screen
        self.pos_x = 400
        self.pos_y = 550

        self.playerImage = pygame.image.load('Images/flatbrick.gif')

        self.playerSpeed = 10

        self.currentBallLimit = 5

        self.ball_list = []

        self.rect = self.playerImage.get_rect()

        self.rect.x = self.pos_x
        self.rect.y = self.pos_y

    # Draw the image on the screen also a debug representation of the collider.
    def draw(self):
        window.blit(self.playerImage, (self.pos_x, self.pos_y))
        pygame.draw.rect(window, red, self.rect, 2)

    # Takes the input and then performs actions based on the inputs.
    def update(self, input):

        if input[K_RIGHT]:
            self.pos_x += self.playerSpeed
            self.rect.x = self.pos_x


        if input[K_LEFT]:
            self.pos_x -= self.playerSpeed
            self.rect.x = self.pos_x

        # Check if the number of balls currently on screen is more than the limit.
        if keysPressed[K_SPACE]:
            if len(self.ball_list) < self.currentBallLimit:
                new_ball = Ball(self.pos_x + 100, 525)
                self.ball_list.append(new_ball)
                activeSpriteList.add(new_ball)
    # Simple get function to return the ball_list for use elsewhere
    def get_ball_list(self):
        return self.ball_list


pygame.init()
width = 800
height = 600

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()
fps = 60

window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Brick Breaking Project")

activeBricksList = pygame.sprite.Group()
activeSpriteList = pygame.sprite.Group()

player = Paddle()


while True:
    keysPressed = pygame.key.get_pressed()

    window.fill(white)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    player.update(keysPressed)
    player.draw()

    for balls in player.get_ball_list():
        balls.draw()
        balls.update(player)
        if balls.rect.colliderect(player):
            balls.speed_y *= -1

    pygame.display.update()
    clock.tick(fps)
