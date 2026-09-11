import pygame
from Display import Simulation

# Display configuration
SCREEN_DIMENSIONS = (640, 480)  # Window size (maintain 4:3 aspect ratio)
CELL_SIZES = (16, 20, 32, 40, 80, 160)  # Available zoom levels (cell sizes in pixels)
CURRENT_ZOOM = 2  # Starting zoom level (index into CELL_SIZES)

# Simulation configuration
SPEEDS = (1, 2, 3, 5, 6, 10, 15, 30)  # Available simulation speeds (updates per render frame)
CURRENT_SPEED = 5  # Starting speed (index into SPEEDS)

# UI configuration
FONT_SIZE = 16  # Font size for text rendering
FRAME_RATE = 30  # Display refresh rate in frames per second

# Initialize pygame and create main window
pygame.init()
display = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Kishal's fraudulent game of life")
clock = pygame.time.Clock() 
font = pygame.font.SysFont("ocraextended", FONT_SIZE, True)  # Font for UI rendering

# Main game loop
def main():
    # Create simulation with all configuration parameters
    simulation_display = Simulation(display, font, SCREEN_DIMENSIONS[0], SCREEN_DIMENSIONS[1], CELL_SIZES, len(CELL_SIZES), CURRENT_ZOOM, SPEEDS, 
                                    len(SPEEDS), CURRENT_SPEED, FRAME_RATE)
    running = True
    frame_count = 0

    # Main game loop: process events, update simulation, and render
    while running:
        frame_count += 1
        events = pygame.event.get()
        running = simulation_display.loop(events, frame_count)
                    
        pygame.display.update()
        clock.tick(FRAME_RATE)  # Limit to target frame rate

    pygame.quit()

# Entry point for the application
if __name__ == "__main__":
    main()