import pygame

# This class will be used to act as a visual indicator for when the simulation is active or not
class StatusSymbol:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.colour = self.red

    def flip_states(self, state):
        if not state:
            self.colour = self.green
        else:
            self.colour = self.red

    def draw_status(self, display):
        pygame.draw.circle(display, self.colour, self.center, self.radius)
        pygame.draw.circle(display, (0,0,0), self.center, self.radius, width=3)