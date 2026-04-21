#The student version of Snake to be completed as an exercise
import pygame
from random import randint as rn

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 900
HEIGHT = 600
CELL_SIZE = 10
direction = "RIGHT"


win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Day 1")


# Grid dimensions
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Snake (length 5 with a bend)
snake = [
    (10, 13),
    (10, 12),
    (10, 11),
    (10, 10),  # head
    (9, 10),
    (8, 10),
    (8, 11),
    (8, 12)   # tail
]

# Convert grid position to screen position
def grid_to_screen(pos):
    x, y = pos
    return (x * CELL_SIZE, y * CELL_SIZE)

# Draw debug grid
def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(win, (50, 50, 50), (x, 0), (x, HEIGHT))

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(win, (50, 50, 50), (0, y), (WIDTH, y))

# Draw the snake
def draw_snake():
    for segment in snake:
        x, y = grid_to_screen(segment)
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(win, (0, 200, 0), rect)

def move_snake(direction, snake):
    #TASK A - MOVE THE SNAKE IN THE CURRENT DIRECTION
    #TODO
    pass 

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # TASK BHANDLE KEY PRESSES FOR DIRECTION CHANGE
        #TO DO
        
    # TASK C - CHECK FOR OUT OF BOUNDS CONDITIONS
    #TO DO


    # Clear screen
    win.fill((30, 30, 30))

    # Draw elements
    draw_snake()
    move_snake(direction, snake)

    # Update display
    pygame.display.update()

pygame.quit()
