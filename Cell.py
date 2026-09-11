import pygame

# List of coordinate offsets representing the 8 adjacent neighbors (up, down, left, right, and diagonals)
OFFSETS = [[0, -1], [0, 1], [1, 0], [-1, 0], [-1, -1], [1, -1], [-1, 1], [1, 1]]

# Represents a single cell in Conway's Game of Life grid
class Cell:
    # Constructor: Initialize a cell with grid position, size, and alive state
    def __init__(self, x, y, cell_size):
        self.x = x  # X coordinate in the grid
        self.y = y  # Y coordinate in the grid
        self.cell_size = cell_size  # Size of the cell in pixels
        self.alive = True  # Cell starts alive by default
        self.colour = (0,0,0)  # Color of the cell (black for alive)

    # Count alive neighbors and track dead cells that have alive neighbors
    # Returns list of alive neighbor cells; updates dead_cells dictionary to track potential resurrections
    def check_neighbours(self, map_object, dead_cells):
        # dead_cells dict tracks dead cells and their living neighbor count (for resurrection)
        neighbours = []
        # Check all 8 adjacent positions
        for offset in OFFSETS:
            check_x = self.x + offset[0]
            check_y = self.y + offset[1]
            check_key = map_object.generate_key(check_x, check_y)

            if check_key in map_object.map:
                # Add alive neighbor to list
                neighbours.append(map_object.map[check_key])
            else:
                # Track dead cells that are adjacent to alive cells
                if check_key in dead_cells:
                    dead_cells[check_key] += 1
                else:
                    dead_cells[check_key] = 1

        return neighbours

    # Apply Conway's Game of Life rules: cell dies if it has fewer than 2 or more than 3 neighbors
    def update_cell(self, map_object, dead_cells):
        neighbours = self.check_neighbours(map_object, dead_cells)
        length = len(neighbours)

        # Kill cell if it has underpopulation (< 2) or overpopulation (> 3)
        if(length < 2 or length > 3):
            self.alive = False

    # Update the cell's display size (used for zoom in/out)
    def update_cell_size(self, new_cell_size):
        self.cell_size = new_cell_size

    # Render the cell as a rectangle on the display, accounting for camera offset
    def draw_cell(self, display, offset):
        # Convert grid coordinates to screen coordinates
        display_x = (self.x * self.cell_size) + (offset[0] * self.cell_size)
        display_y = (self.y * self.cell_size) + (offset[1] * self.cell_size)
        display_cell = pygame.Rect(display_x, display_y, self.cell_size, self.cell_size)

        # Draw filled rectangle for this cell
        pygame.draw.rect(display, self.colour, display_cell)

    # Check if the cell is currently alive
    def is_alive(self):
        return self.alive