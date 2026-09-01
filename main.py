import pygame
from Display import Simulation

SCREEN_DIMENSIONS = (640, 480)
CELL_SIZE = 32

pygame.init()
display = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Kishal's fraudulent game of life")
clock = pygame.time.Clock()

def main():
    simulation_display = Simulation(display, SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1], CELL_SIZE)
    running = True

    while running:
        events = pygame.event.get()
        running = simulation_display.loop(events)
                    
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()