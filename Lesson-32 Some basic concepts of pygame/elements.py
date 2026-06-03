import sys
import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My First Pygame Screen")
BACKGROUND_COLOR = (30, 30, 40) 
RECT_COLOR = (255, 100, 100)  
TEXT_COLOR = (255, 255, 255) 
font = pygame.font.Font(None, 50)
text_surface = font.render("Hello, Pygame!", True, TEXT_COLOR)


text_rect = text_surface.get_rect()
text_rect.center = (SCREEN_WIDTH // 2, 100)  


my_rectangle = pygame.Rect(300, 250, 200, 150)

clock = pygame.time.Clock()


running = True
while running:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(BACKGROUND_COLOR)

   
    pygame.draw.rect(screen, RECT_COLOR, my_rectangle)

  
    screen.blit(text_surface, text_rect)

  
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()