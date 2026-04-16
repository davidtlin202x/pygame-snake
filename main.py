import pygame

# Initialize pygame
pygame.init()

#TODO - SET UP GAME WINDOW
# Screen settings



# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Grid dimensions
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

# Snake (length 5 with a bend)
snake = [
    (10, 10),  # head
    (9, 10),
    (8, 10),
    (8, 11),
    (8, 12)   # tail
]

# Convert grid position to screen position
def grid_to_screen(pos):
    #TODO - WRITE THIS FUNCTION


# Draw debug grid
def draw_grid():
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(win, (50, 50, 50), (x, 0), (x, SCREEN_HEIGHT))

    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(win, (50, 50, 50), (0, y), (SCREEN_WIDTH, y))


# Draw the snake
def draw_snake():
   #TODO


# Main game loop
running = True

while running:
  #tODO - WRITE THE GAME LOOP

    
