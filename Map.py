from Cell import Cell

class Map:
    def __init__(self, cell_size):
        # The coordinate system for our map will be in line with our grid system
        # To go from screen coords to grid coords, we divide by cell size and for vice versa, we multiply by cell size
        self.map = {} # contains locations of alive cells
        self.cell_size = cell_size
        self.generation = 0

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

    def update_cells(self):
        dead_cells = {}
        new_map = self.map.copy()

        for key in self.map:
            cell = self.map[key]
            cell.update_cell(self, dead_cells)

            if not cell.is_alive():
                del new_map[key]

        for cell in dead_cells:
            count = dead_cells[cell]

            if count == 3:
                coords = cell.split(":")
                new_x = int(coords[0])
                new_y = int(coords[1])
                new_cell = Cell(new_x, new_y, self.cell_size)

                new_map[cell] = new_cell

        self.map = new_map

    def get_population(self):
        return len(self.map)

    def update_generation(self):
        self.generation += 1

    def get_generation(self):
        return self.generation

    def draw_map(self, display, offset):
        for key in self.map:
            cell = self.map[key]

            cell.draw_cell(display, offset)