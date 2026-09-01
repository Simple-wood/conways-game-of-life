import pygame
from Map import Map

class Display:
    def __init__(self, display, width, height):
        self.display = display
        self.display_height = height
        self.display_width = width
        self.offset = [0,0]

    def update_offset(self, x=0, y=0):
        self.offset[0] += x
        self.offset[1] += y


class Simulation(Display):
    def __init__(self, display, width, height, cell_size):
        super().__init__(display, width, height)
        self.directions = [0,0]
        self.cell_size = cell_size

        self.map = Map(self.cell_size)
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

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_a, pygame.K_d]:
                    self.directions[0] = 0
                elif event.key in [pygame.K_w, pygame.K_s]:
                    self.directions[1] = 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                    self.map.add_cell(grid_coords[0], grid_coords[1])
                elif event.button == 3:
                    grid_coords = self.map.to_grid_coordinates(event.pos[0], event.pos[1], self.offset)
                    self.map.remove_cell(grid_coords[0], grid_coords[1])

        return True

    def draw_grid(self):
        for x in range(0, self.display_width, self.cell_size):
            for y in range(0, self.display_height, self.cell_size):
                grid_box = pygame.Rect(x, y, self.cell_size, self.cell_size)
                pygame.draw.rect(self.display, (196, 196, 196), grid_box, 2)

    def refresh_screen(self):
        self.display.fill((255, 255, 255))
        self.map.draw_map(self.display, self.offset)      
        self.draw_grid()

    def loop(self, events):
        self.refresh_screen()
        self.update_offset_directions()
        return self.handle_events(events)