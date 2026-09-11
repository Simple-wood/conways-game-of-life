import pygame
from Display import Simulation

SCREEN_DIMENSIONS = (640, 480)
CELL_SIZES = (16, 20, 32, 40, 80, 160)
SPEEDS = (1, 2, 3, 5, 6, 10, 15, 30)
FONT_SIZE = 16
FRAME_RATE = 30

pygame.init()
display = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Kishal's fraudulent game of life")
clock = pygame.time.Clock()
font = pygame.font.SysFont("ocraextended", FONT_SIZE, True)

def main():
    simulation_display = Simulation(display, font, SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1], CELL_SIZES, len(CELL_SIZES), 2, SPEEDS, 
                                    len(SPEEDS), 5, FRAME_RATE)
    running = True
    frame_count = 0

    while running:
        frame_count += 1
        events = pygame.event.get()
        running = simulation_display.loop(events, frame_count)
                    
        pygame.display.update()
        clock.tick(FRAME_RATE)

    pygame.quit()

if __name__ == "__main__":
    main()