import pygame

# Visual indicator that shows whether the simulation is in creation mode (red) or running (green)
class StatusSymbol:
    # Initialize status indicator at specified position
    def __init__(self, center, radius):
        self.center = center  # (x, y) position on screen
        self.radius = radius  # Circle radius in pixels
        self.red = (255, 0, 0)  # Color for creation mode
        self.green = (0, 255, 0)  # Color for simulation mode
        self.colour = self.red  # Start in creation mode (red)

    # Update indicator color based on simulation state
    def flip_states(self, state):
        # state=True means creation mode (red), state=False means simulation running (green)
        self.colour = self.green if not state else self.red

    # Render the status indicator as a filled circle with black outline
    def draw_status(self, display):
        pygame.draw.circle(display, self.colour, self.center, self.radius)  # Filled circle
        pygame.draw.circle(display, (0,0,0), self.center, self.radius, width=3)  # Black outline