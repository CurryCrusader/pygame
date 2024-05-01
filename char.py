import pygame
balloonImage = 0
balloonRect = 0
blimpImage = 0
blimpImage = 0
blimpRect = 0
boomerangImage = 0
boomerangImage = 0
boomerangRect = 0
dartImage = 0
dartImage = 0
dartRect = 0
laserImage = 0
laserImage = 0
laserRect = 0
monkey1Image = 0
monkey1Image = 0
monkey1Rect = 0
monkey2Image = 0
monkey2Image = 0
monkey2Rect = 0
monkey3Image = 0
monkey3Rect = 0

def load_characters(): 
    global balloonImage, balloonRect, blimpImage, blimpRect, boomerangImage, boomerangRect, dartImage, dartRect, laserImage, laserRect, monkey1Image, monkey1Rect, monkey2Image, monkey2Rect, monkey3Image, monkey3Rect
    balloonImage = pygame.image.load("balloon.jpg")
    balloonImage = pygame.transform.scale(balloonImage, (500, 500))
    balloonRect = balloonImage.get_rect()
    balloonRect.x = 500
    balloonRect.y = 500 
    blimpImage = pygame.image.load("blimp.jpg")
    blimpImage = pygame.transform.scale(blimpImage, (50, 50))
    blimpRect = blimpImage.get_rect()
    boomerangImage = pygame.image.load("boomerang.webp")
    boomerangImage = pygame.transform.scale(boomerangImage, (50, 50))
    boomerangRect = boomerangImage.get_rect()
    dartImage = pygame.image.load("dart.png")
    dartImage = pygame.transform.scale(dartImage, (50, 50))
    dartRect = dartImage.get_rect()
    laserImage = pygame.image.load("laser.webp")
    laserImage = pygame.transform.scale(laserImage, (50, 50))
    laserRect = laserImage.get_rect()
    monkey1Image = pygame.image.load("monkey1.jpg")
    monkey1Image = pygame.transform.scale(monkey1Image, (50, 50))
    monkey1Rect = monkey1Image.get_rect()
    monkey2Image = pygame.image.load("monkey2.jpg")
    monkey2Image = pygame.transform.scale(monkey2Image, (50, 50))
    monkey2Rect = monkey2Image.get_rect()
    monkey3Image = pygame.image.load("monkey3.jpg")
    monkey3Image = pygame.transform.scale(monkey3Image, (50, 50))
    monkey3Rect = monkey3Image.get_rect()


