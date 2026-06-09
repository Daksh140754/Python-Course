import math
import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40

BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))

background = pygame.image.load('Background.jpg')

pygame.display.set_caption("Space Invader")
icon = pygame.image.load('Ufo.png')
pygame.display.set_icon(icon)

playerimg = pygame.image.load('Player.jpeg')
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
    enemyimg.append(pygame.image.load('Enemy.png'))
    enemyx.append(random.randint(0 , SCREEN_WIDTH - 64))

    enemyy.append(random.randint(ENEMY_START_Y_MIN , ENEMY_START_Y_MAX))
    enemy_Xchange.append(ENEMY_SPEED_X)
    enemy_Ychange.append(ENEMY_SPEED_Y)

bulletimg = pygame.image.load('Bullet.png')
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
    game_over_text = over_font.render("GAME OVER" , True , (255 , 255 , 255))
    screen.blit(game_over_text , (200 , 250))

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


running =True
while running:
    screen.fill((0 , 0 , 0))
    screen.blit(background , (0 , 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_Change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletx = playerX
                fire_bullet(bulletx , bullety)

        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT , pygame.K_RIGHT]:
            playerX_Change = 0

    playerX += playerX_Change
    playerX = max(0 , min(playerX , SCREEN_WIDTH -64))


    for i in range(num_of_enemies):
        if enemyy[i] > 340:
            for j in range(num_of_enemies):
                enemyy[j] = 2000

            game_over()
            break

        enemyx[i] += enemy_Xchange[i]

        if enemyx[i] <= 0 or enemyx[i] >= SCREEN_WIDTH - 64:
            enemy_Xchange[i] *= -1
            enemyy[i] += enemy_Ychange[i]


        if iscollison(enemyx[i] , enemyy[i] , bulletx , bullety):
            bullety = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyx[i] = random.randint (0 , SCREEN_WIDTH - 64)
            

            enemyy[i] = random.randint(ENEMY_START_Y_MIN , ENEMY_START_Y_MAX)

        enemy(enemyx[i] , enemyy[i] , i)


    if bullety <= 0:
        bullety - PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletx , bullety)
        bullety -= bulletY_change


player(playerX , playerY)
show_score(textX , textY)
pygame.display.update()



