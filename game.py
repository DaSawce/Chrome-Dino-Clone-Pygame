import pygame
import os

#INITIALIZE PYGAME TO PROGRAM
pygame.init()

#MUST SET SCREEN SIZES
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100

SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

START = pygame.image.load(os.path.join("Assets/Dino", "DinoStart.png"))
DEAD = pygame.image.load(os.path.join("Assets/Dino", "DinoDead.png"))

#LOAD SPRITES WITH ITS OWN PICTURES FROM ASSETS FOLDER
RUNNING = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png"))]

JUMPING = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))

DUCKING = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
           pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]

BIRD = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")),
           pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]

SMALL_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

LARGE_CACTUS = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
           pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

BACKGROUND = pygame.image.load(os.path.join("Assets/Other", "Track.png"))


class Dinosaur:
    X_POSITION =
    Y_POSITION =

#LOOP TO RUN GAME 
def main():
    run = True
    clock=pygame.time.Clock()
    player = Dinosaur()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        SCREEN.fill((255, 255, 255))
        userInput = pygame.key.get_pressed()

        player.draw(SCREEN)
        player.update(userInput)

        clock.tick(60)
        pygame.display.update