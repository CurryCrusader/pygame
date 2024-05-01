import pygame
def startscreen():
    startImage = 0
    startRect = 0
    start = True
    while start:
        startImage = pygame.image.load("start.jpg")
        startImage = pygame.transform.scale(startImage, (500, 500))
        startRect = startImage.get_rect()