import pygame
pygame.init()
import random

grass = pygame.image.load("./assets/bg.jpg")
road = pygame.image.load("./assets/road.png")
yellow_car = pygame.image.load("./assets/yellow_car.png")
red_car = pygame.image.load("./assets/red_car.png")
yellow_car = pygame.transform.rotate(yellow_car, 90)
yellow_car = pygame.transform.scale(yellow_car, (60, 100))
red_car = pygame.transform.scale(red_car, (110, 100))
red_car = pygame.transform.rotate(red_car, 180)
grass = pygame.transform.scale(grass, (600, 600))
road = pygame.transform.rotate(road, 90)
road = pygame.transform.scale(road, (500, 1650))
screen = pygame.display.set_mode((600, 600))

GAME_RUNNING = True
yellow_x = 280
yellow_y = 480
red_x = 330
red_y = -100
while GAME_RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GAME_RUNNING = False
            if event.key == pygame.K_LEFT and yellow_x != 190:
                yellow_x = yellow_x - 10
            if event.key == pygame.K_RIGHT and yellow_x != 350:
                yellow_x = yellow_x + 10
    screen.blit(grass, (0,0))
    screen.blit(road, (50, -20))
    screen.blit(yellow_car, (yellow_x,yellow_y))
    screen.blit(red_car, (red_x, red_y))
    red_y += 1
    if(red_y>600):
        red_y = -100
        red_x = random.randrange(100, 330)
        if(red_x>=yellow_x-20 and red_x<=yellow_x+20):
            GAME_RUNNING = False
    pygame.display.update()