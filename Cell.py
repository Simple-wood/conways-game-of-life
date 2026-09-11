import pygame

# [x, y] offsets
OFFSETS = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1]]

class Cell:
    def __init__(self, x, y, cell_size):
        self.x = x
        self.y = y
        self.cell_size = cell_size
        self.alive = True
        self.colour = (0,0,0)

    def check_neighbours(self, map_object, dead_cells):
        # dead_cell = {key, value}
        # key in format "x:y", value represents a number
        neighbours = []
        for offset in OFFSETS:
            check_x = self.x + offset[0]
            check_y = self.y + offset[1]
            check_key = map_object.generate_key(check_x, check_y)

            if check_key in map_object.map:
                # We have an alive cell 
                neighbours.append(map_object.map[check_key])
            else:
                if check_key in dead_cells:
                    count = dead_cells[check_key] + 1
                    dead_cells[check_key] = count
                else:
                    dead_cells[check_key] = 1

        return neighbours

    def update_cell(self, map_object, dead_cells):
        neighbours = self.check_neighbours(map_object, dead_cells)
        length = len(neighbours)

        if(length < 2 or length > 3):
            self.alive = False

    def update_cell_size(self, new_cell_size):
        self.cell_size = new_cell_size

    def draw_cell(self, display, offset):
        display_x = (self.x * self.cell_size) + (offset[0] * self.cell_size)
        display_y = (self.y * self.cell_size) + (offset[1] * self.cell_size)
        display_cell = pygame.Rect(display_x, display_y, self.cell_size, self.cell_size)

        pygame.draw.rect(display, self.colour, display_cell)

    def is_alive(self):
        return self.alive