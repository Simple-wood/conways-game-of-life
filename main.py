import pygame

SCREEN_DIMENSIONS = (640, 480)

pygame.init()
display = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Kishal's fraudulent game of life")
clock = pygame.time.Clock()

def main():
    running = True
    display.fill((0,0,0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()