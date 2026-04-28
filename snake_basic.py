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
pygame.display.set_caption("Snake Game - Day 4")


# Grid dimensions
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

# Snake
snake = [
    (10, 13),
    (10, 12),
    (10, 11),
    (10, 10),
    (9, 10),
    (8, 10),
    (8, 11),
    (8, 12)
]

score = 0

# Convert grid position to screen position
def grid_to_screen(pos):
    x, y = pos
    return (x * CELL_SIZE, y * CELL_SIZE)

# Draw the snake
def draw_snake():
    for segment in snake:
        x, y = grid_to_screen(segment)
        rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(win, (0, 200, 0), rect)

# Draw score
def draw_score():
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    win.blit(text, (10, 10))

# Main game loop
clock = pygame.time.Clock()
running = True
message = ""

while running:
    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Check wall collision
    if snake[0][0] < 0 or snake[0][0] >= GRID_WIDTH or snake[0][1] < 0 or snake[0][1] >= GRID_HEIGHT:
        message = "OUT OF BOUNDS!"
        running = False

    # Check self collision
    if snake[0] in snake[1:]:
        message = "YOU RAN INTO YOURSELF!"
        running = False

    # Clear screen
    win.fill((30, 30, 30))

    # Draw elements
    draw_snake()
    draw_score()

    pygame.display.update()

# Show Game Over screen
