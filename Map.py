from Cell import Cell

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
        cell = Cell(x, y, self.cell_size)

        self.map[key] = cell

    def remove_cell(self, x, y):
        key = self.generate_key(x, y)

        if key in self.map:
            del self.map[key]

    def draw_map(self, display, offset):
        for key in self.map:
            cell = self.map[key]

            cell.draw_cell(display, offset)