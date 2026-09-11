import pygame
from Map import Map
from utils import StatusSymbol

BORDER_COLOUR = (196, 196, 196)
TEXT_COLOUR = (0, 180, 17)
BACKGROUND_COLOUR = (255, 255, 255)

# Base display class for managing the pygame window and camera offset
class Display:
    # Initialize display properties including window dimensions and camera offset
    def __init__(self, display, font, width, height):
        self.display = display  # Pygame display surface
        self.font = font  # Font for text rendering
        self.display_height = height  # Window height in pixels
        self.display_width = width  # Window width in pixels
        self.offset = [0,0]  # Camera offset in grid units [x, y]

    # Update camera offset (used for panning the view)
    def update_offset(self, x=0, y=0):
        self.offset[0] += x  # Adjust horizontal camera position
        self.offset[1] += y  # Adjust vertical camera position


# Main simulation class that extends Display; handles the game loop and user input
class Simulation(Display):
    # Initialize simulation with display, cell size options, and speed options
    def __init__(self, display, font, width, height, cell_sizes, option_count, cell_pointer, speeds, speed_count, speed_pointer, frame_rate):
        super().__init__(display, font, width, height)
        self.directions = [0,0]  # Current panning direction [x, y]

        # Zoom levels: list of available cell sizes and current selection
        self.cell_sizes = cell_sizes
        self.option_count = option_count  # Number of zoom options
        self.cell_pointer = cell_pointer  # Current zoom level index
        self.cell_size = self.cell_sizes[self.cell_pointer]  # Current cell size in pixels

        # Simulation speed: list of available frame rates and current selection
        self.speeds = speeds  # Possible simulation speeds
        self.speed_count = speed_count  # Number of speed options
        self.speed_pointer = speed_pointer  # Current speed index
        self.speed = self.speeds[self.speed_pointer]  # Current frames per generation

        self.fps = frame_rate  # Display frame rate

        # Game state
        self.map = Map(self.cell_size)  # Grid containing all cells

        #hardcoded evil ik
        self.indicator = StatusSymbol((30, 110), 20)  # Visual indicator showing if paused/running
        self.state = True  # True = creation mode (place cells), False = simulation mode (running)

    # Apply continuous camera movement based on directional input
    def update_offset_directions(self):
        # directions[0] = horizontal movement, directions[1] = vertical movement
        self.offset[0] += self.directions[0]
        self.offset[1] += self.directions[1]

    # Process keyboard and mouse input events (camera movement, zoom, cell placement)
    def handle_events(self, events):
        # Handle all pygame events for the frame
        for event in events:
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                # SPACE toggles between creation mode and simulation mode
                if event.key == pygame.K_SPACE:
                    self.state = not self.state
                    self.indicator.flip_states(self.state)

                # A/D keys set continuous horizontal panning
                if event.key == pygame.K_a:
                    self.directions[0] = 1
                elif event.key == pygame.K_d:
                    self.directions[0] = -1
                # W/S keys set continuous vertical panning
                elif event.key == pygame.K_w:
                    self.directions[1] = 1
                elif event.key == pygame.K_s:
                    self.directions[1] = -1

                # Arrow keys for one-time camera adjustments
                elif event.key == pygame.K_LEFT:
                    self.update_offset(x=1)
                elif event.key == pygame.K_RIGHT:
                    self.update_offset(x=-1)
                elif event.key == pygame.K_UP:
                    self.update_offset(y=1)
                elif event.key == pygame.K_DOWN:
                    self.update_offset(y=-1)

                # Comma/Period keys adjust simulation speed
                elif event.key == pygame.K_COMMA:
                    self.increase_speed()
                    self.speed = self.speeds[self.speed_pointer]
                elif event.key == pygame.K_PERIOD:
                    self.decrease_speed()
                    self.speed = self.speeds[self.speed_pointer]

            elif event.type == pygame.KEYUP:
                # Stop panning when key is released
                if event.key in [pygame.K_a, pygame.K_d]:
                    self.directions[0] = 0
                elif event.key in [pygame.K_w, pygame.K_s]:
                    self.directions[1] = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # In creation mode: left click adds cell, right click removes cell
                if self.state:
                    if event.button == 1:
                        grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                        self.map.add_cell(grid_coords[0], grid_coords[1])
                    elif event.button == 3:
                        grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                        self.map.remove_cell(grid_coords[0], grid_coords[1])

                # Mouse wheel adjusts zoom level
                if event.button == 4:
                    self.increase_zoom()
                    self.update_cell_sizes()
                elif event.button == 5:
                    self.decrease_zoom()
                    self.update_cell_sizes()

        return True

    def update_cell_sizes(self):
        self.cell_size = self.cell_sizes[self.cell_pointer]
        self.map.update_cell_size(self.cell_size)

    def increase_zoom(self):
        self.cell_pointer = min(self.option_count - 1, self.cell_pointer + 1)

    def decrease_zoom(self):
        self.cell_pointer = max(0, self.cell_pointer - 1)

    def increase_speed(self):
        self.speed_pointer = min(self.speed_count - 1, self.speed_pointer + 1)

    def decrease_speed(self):
        self.speed_pointer = max(0, self.speed_pointer - 1)

    def draw_grid(self):
        for x in range(0, self.display_width, self.cell_size):
            for y in range(0, self.display_height, self.cell_size):
                grid_box = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.display, BORDER_COLOUR, grid_box, 2)

    def calculate_speed(self):
        speed = self.fps // self.speed
        speed_text = str(speed) + "x"

        return speed_text

    def draw_statistics(self):
        generation_text = "Generation : " + str(self.map.get_generation())
        population_text = "Population : " + str(self.map.get_population())
        speed_text = self.calculate_speed()

        render_pop_text = self.font.render(population_text, True, TEXT_COLOUR)
        render_gen_text = self.font.render(generation_text, True, TEXT_COLOUR)
        render_speed_text = self.font.render(speed_text, True, TEXT_COLOUR)

        # also more hardcoded evil, iknow
        self.display.blit(render_gen_text, (5, 10))
        self.display.blit(render_pop_text, (5, 36))
        self.display.blit(render_speed_text, (5, 62))

    def refresh_screen(self):
        self.display.fill(BACKGROUND_COLOUR)
        self.map.draw_map(self.display, self.offset)      
        self.draw_grid()
        self.draw_statistics()
        self.indicator.draw_status(self.display)

    def loop(self, events, count):
        self.refresh_screen()
        self.update_offset_directions()

        if not self.state and count % self.speed == 0:
            self.map.update_cells()
            self.map.update_generation()

        return self.handle_events(events)