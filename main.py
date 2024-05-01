import pygame
import random
import char
import start
ScreenWidth=1920
ScreenHeight=1080
screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

char.load_characters()
start.startscreen()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    screen.blit(char.balloonImage, char.balloonRect)
    pygame.display.flip()

pygame.quit()



























running=True
while running:
    screen.fill((255, 255, 255))
    pygame.display.flip



