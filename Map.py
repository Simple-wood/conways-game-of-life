from Cell import Cell

# Manages the grid of cells for Conway's Game of Life
class Map:
    # Initialize empty grid with given cell size and generation counter
    def __init__(self, cell_size):
        # Note: Grid coordinate system - screen coords = grid coords * cell_size (and vice versa)
        self.map = {}  # Dictionary storing alive cells as {"x:y": Cell object}
        self.cell_size = cell_size  # Size of each cell in pixels
        self.generation = 0  # Tracks which generation of the simulation we're on

    # Convert screen pixel coordinates to grid coordinates, accounting for camera offset
    def to_grid_coordinates(self, x, y, offset):
        new_x = (x - (offset[0] * self.cell_size)) // self.cell_size
        new_y = (y - (offset[1] * self.cell_size)) // self.cell_size

        return [new_x, new_y]

    # Generate string key for storing a cell in the map dictionary
    def generate_key(self, x, y):
        return str(x) + ":" + str(y)

    # Add a new live cell at the specified grid coordinates
    def add_cell(self, x, y):
        key = self.generate_key(x, y)
        cell = Cell(x, y, self.cell_size)
        self.map[key] = cell

    # Remove a live cell from the grid
    def remove_cell(self, x, y):
        key = self.generate_key(x, y)
        if key in self.map:
            del self.map[key]

    # Apply Conway's Game of Life rules to all cells (main simulation step)
    def update_cells(self):
        dead_cells = {}  # Track dead cells that might resurrect (exactly 3 neighbors)
        new_map = self.map.copy()  # Start with current cells

        # Step 1: Update all alive cells and track dead cells adjacent to them
        for key in self.map:
            cell = self.map[key]
            cell.update_cell(self, dead_cells)  # Apply survival rules

            # Remove cells that died
            if not cell.is_alive():
                del new_map[key]

        # Step 2: Check for dead cells that should become alive (exactly 3 alive neighbors)
        for cell in dead_cells:
            count = dead_cells[cell]

            if count == 3:
                # Resurrect cell if it had exactly 3 neighbors
                coords = cell.split(":")
                new_x = int(coords[0])
                new_y = int(coords[1])
                new_cell = Cell(new_x, new_y, self.cell_size)
                new_map[cell] = new_cell

        self.map = new_map

    # Update cell display size when zoom changes (affects all cells in grid)
    def update_cell_size(self, new_size):
        self.cell_size = new_size
        for key in self.map:
            cell = self.map[key]
            cell.update_cell_size(new_size)

    # Get the number of currently alive cells
    def get_population(self):
        return len(self.map)

    # Increment generation counter after each simulation step
    def update_generation(self):
        self.generation += 1

    # Get current generation number
    def get_generation(self):
        return self.generation

    # Render all cells in the grid to the display
    def draw_map(self, display, offset):
        for key in self.map:
            cell = self.map[key]
            cell.draw_cell(display, offset)