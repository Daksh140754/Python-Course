import pygame
import sys
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprite Movement Example")
BACKGROUND_COLOR = (30, 30, 30)     
PLAYER_COLOR = (0, 255, 128)        
OBSTACLE_COLOR = (255, 85, 85)      


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed):
        super().__init__()
      
        self.image = pygame.Surface([width, height])
        self.image.fill(PLAYER_COLOR)
        
       
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        """Handle player movement based on key presses."""
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(OBSTACLE_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




player = Player(x=100, y=100, width=50, height=50, speed=5)
obstacle = Obstacle(x=400, y=250, width=120, height=80)


all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(obstacle)


clock = pygame.tracker = pygame.time.Clock()


running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

  
    all_sprites.update()

  
    screen.fill(BACKGROUND_COLOR)  
    all_sprites.draw(screen)       
    pygame.display.flip()          

  
    clock.tick(60)

pygame.quit()
sys.exit()