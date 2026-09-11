import pygame
from Map import Map
from utils import StatusSymbol

class Display:
    def __init__(self, display, font, width, height):
        self.display = display
        self.font = font
        self.display_height = height
        self.display_width = width
        self.offset = [0,0]

    def update_offset(self, x=0, y=0):
        self.offset[0] += x
        self.offset[1] += y


class Simulation(Display):
    def __init__(self, display, font, width, height, cell_sizes, option_count, cell_pointer, speeds, speed_count, speed_pointer, frame_rate):
        super().__init__(display, font, width, height)
        self.directions = [0,0]

        self.cell_sizes = cell_sizes
        self.option_count = option_count
        self.cell_pointer = cell_pointer
        self.cell_size = self.cell_sizes[self.cell_pointer]

        self.speeds = speeds
        self.speed_count = speed_count
        self.speed_pointer = speed_pointer
        self.speed = self.speeds[self.speed_pointer]

        self.fps = frame_rate

        self.map = Map(self.cell_size)
        self.indicator = StatusSymbol((30, 110), 20)
        self.state = True # boolean flag - if true we are in creation state else we are in simulation state

    def update_offset_directions(self):
        # directions is an array of length 2 [x_direction, y_direction]
        self.offset[0] += self.directions[0]
        self.offset[1] += self.directions[1]

    def handle_events(self, events):
        # this handles camera movement
        for event in events:
            if event.type == pygame.QUIT:
                return False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.state = not self.state
                    self.indicator.flip_states(self.state)

                if event.key == pygame.K_a:
                    self.directions[0] = 1
                elif event.key == pygame.K_d:
                    self.directions[0] = -1
                elif event.key == pygame.K_w:
                    self.directions[1] = 1
                elif event.key == pygame.K_s:
                    self.directions[1] = -1

                elif event.key == pygame.K_LEFT:
                    self.update_offset(x=1)
                elif event.key == pygame.K_RIGHT:
                    self.update_offset(x=-1)
                elif event.key == pygame.K_UP:
                    self.update_offset(y=1)
                elif event.key == pygame.K_DOWN:
                    self.update_offset(y=-1)

                elif event.key == pygame.K_COMMA:
                    self.increase_speed()
                    self.speed = self.speeds[self.speed_pointer]
                elif event.key == pygame.K_PERIOD:
                    self.decrease_speed()
                    self.speed = self.speeds[self.speed_pointer]

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:
                    self.directions[0] = 0
                elif event.key in [pygame.K_w, pygame.K_s]:
                    self.directions[1] = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.state:
                    if event.button == 1:
                        grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                        self.map.add_cell(grid_coords[0], grid_coords[1])
                    elif event.button == 3:
                        grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                        self.map.remove_cell(grid_coords[0], grid_coords[1])

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
                pygame.draw.rect(self.display, (196, 196, 196), grid_box, 2)

    def calculate_speed(self):
        speed = self.fps // self.speed
        speed_text = str(speed) + "x"

        return speed_text

    def draw_statistics(self):
        generation_text = "Generation : " + str(self.map.get_generation())
        population_text = "Population : " + str(self.map.get_population())
        speed_text = self.calculate_speed()

        render_pop_text = self.font.render(population_text, True, (0, 180, 17))
        render_gen_text = self.font.render(generation_text, True, (0, 180, 17))
        render_speed_text = self.font.render(speed_text, True, (0, 180, 17))

        self.display.blit(render_gen_text, (5, 10))
        self.display.blit(render_pop_text, (5, 36))
        self.display.blit(render_speed_text, (5, 62))

    def refresh_screen(self):
        self.display.fill((255,255,255))
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