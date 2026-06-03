import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Batman Hello World") 


Batman_image = pygame.transform.scale(
    pygame.image.load("Batman.JPG").convert_alpha(), (200, 200)
)
Batman_rect = Batman_image.get_rect(
    center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30)
)

text = pygame.font.Font(None, 36).render("Hello World", True, pygame.Color("Black"))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))


def game_loop():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            display_surface.fill(pygame.Color("white"))
        display_surface.blit(Batman_image, Batman_rect)
        display_surface.blit(text, text_rect)

      
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    game_loop()
