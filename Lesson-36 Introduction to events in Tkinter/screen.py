import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame Image Example")

my_image = pygame.image.load("Batman.jpg")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((34, 139, 34))


    screen.blit(my_image, (350, 250))

    pygame.display.flip()

pygame.quit()
