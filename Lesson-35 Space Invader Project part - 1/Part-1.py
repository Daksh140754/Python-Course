import math
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380

ENTER_START_Y_MIN = 50
ENTER_START_Y_MAX = 150

ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40

BULLET_SPEED = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

background = pygame.image.load('')

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('')
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_Change = 0

enemyimg = []
enemyx = []
enemyy = []
enemy_Xchange = []
enemy_Ychange = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(''))
    enemyx.append(random.randint(0 , SCREEN_WIDTH - 64))

    enemyy.append(random.randint(ENTER_START_Y_MIN , ENTER_START_Y_MAX))
    enemy_Xchange.append(ENEMY_SPEED_X)
    enemy_Ychange.append(ENEMY_SPEED_Y)

bulletimg = pygame.image.load('')
bulletx = 0
bullety = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"


score_value = 0
font = pygame.font.Font("freesansbold.ttf" , 32)
textX = 10
textY = 10

over_font = pygame.font.Font("freesansbold.ttf" , 64)

def show_score(x , y):
    score  = font.render("Score:" , + str(score_value) , True , (255 , 255 , 255))
    screen.blit(score , (x , y))

def game_over():
    over_text = over_font.render("GAME OVER" , True , (255 , 255 , 255))
    screen.blit(over_text , (200 , 250))

def player(x , y):
    screen.blit(playerimg , (x , y))

def enemy(x , y):
    screen.blit(enemyimg[i] , (x , y))

def fire_bullet(x , y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg , (x+16) , (y+10))

def iscollison(enemyx , enemyy , bulletx , bullety):
    distance = math.sqrt((enemyx - bulletx)**2 + (enemyy - bullety) **2)
    return distance < COLLISION_DISTANCE


