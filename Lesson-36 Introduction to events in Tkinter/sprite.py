import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Custom Event Color Change")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)

class SquareSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def change_color(self):
        random_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(random_color)

sprite1 = SquareSprite(200, 250)
sprite2 = SquareSprite(500, 250)
sprite_group = pygame.sprite.Group(sprite1, sprite2)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in sprite_group:
                sprite.change_color()

    screen.fill((30, 30, 30))
    sprite_group.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()