import pygame

class Map:
    def __init__(self, cell_size):
        # The coordinate system for our map will be in line with our grid system
        # To go from screen coords to grid coords, we divide by cell size and for vice versa, we multiply by cell size
        self.map = {} # contains locations of alive cells
        self.cell_size = cell_size

    def to_grid_coordinates(self, x, y, offset):
        new_x = (x - (offset[0] * self.cell_size)) // self.cell_size
        new_y = (y - (offset[1] * self.cell_size)) // self.cell_size

        new_coords = [new_x, new_y]
        return new_coords

    def generate_key(self, x, y):
        key = str(x) + ":" + str(y)

        return key

    def add_cell(self, x, y):
        key = self.generate_key(x, y)

        self.map[key] = [x, y]

    def draw_map(self, display, offset):
        for key in self.map:
            coords = self.map[key]
            display_x = (coords[0] * self.cell_size) + (offset[0] * self.cell_size)
            display_y = (coords[1] * self.cell_size) + (offset[1] * self.cell_size)

            cell_rect = pygame.Rect(display_x, display_y, self.cell_size, self.cell_size)
            pygame.draw.rect(display, (0,0,0), cell_rect)