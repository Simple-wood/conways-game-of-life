import pygame

SCREEN_DIMENSIONS = (640, 480)
CELL_SIZE = 32

pygame.init()
display = pygame.display.set_mode(SCREEN_DIMENSIONS)
pygame.display.set_caption("Kishal's fraudulent game of life")
clock = pygame.time.Clock()

def main():
    cells = []
    offset = [0, 0]
    directions = [0, 0]
    running = True

    while running:
        display.fill((255,255,255))

        for cell in cells:
            r = pygame.Rect(cell[0]*32 + (offset[0] * 32), cell[1]*32 + (offset[1] * 32), 32, 32)
            pygame.draw.rect(display, (0,0,0), r)

        for x in range(0, SCREEN_DIMENSIONS[0], 32):
            for y in range(0, SCREEN_DIMENSIONS[1], 32):
                rect = pygame.Rect(x, y, 32, 32)
                pygame.draw.rect(display, (196,196,196), rect, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = (event.pos[0] - (offset[0] * 32)) // 32
                    y = (event.pos[1] - (offset[1] * 32)) // 32

                    cells.append([x, y])

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    directions[0] = 1 
                elif event.key == pygame.K_d:
                    directions[0] = -1
                elif event.key == pygame.K_w:
                    directions[1] = 1
                elif event.key == pygame.K_s:
                    directions[1] = -1

                elif event.key == pygame.K_LEFT:
                    offset[0] += 1
                elif event.key == pygame.K_RIGHT:
                    offset[0] -= 1
                elif event.key == pygame.K_UP:
                    offset[1] += 1
                elif event.key == pygame.K_DOWN:
                    offset[1] -= 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    directions[0] = 0
                elif event.key == pygame.K_d:
                    directions[0] = 0
                elif event.key == pygame.K_w:
                    directions[1] = 0
                elif event.key == pygame.K_s:
                    directions[1] = 0

        offset[0] += directions[0]
        offset[1] += directions[1]
                    
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()