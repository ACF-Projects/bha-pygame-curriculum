"""
We've covered drawing, moving, clocks, collisions,
and classes! Here is one example project: Snake.
"""

import pygame
import snake

pygame.init()

### Variables to set up the game's state! ###
GRID_SIZE = 15  # How many "tiles" are on the board
SQUARE_SIZE = 25  # How many pixels each "tile" is

screen = pygame.display.set_mode((GRID_SIZE * SQUARE_SIZE, GRID_SIZE * SQUARE_SIZE))
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

my_snake = snake.Snake(screen, GRID_SIZE, SQUARE_SIZE)

running = True

while running:

    clock.tick(9)
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### This is just for fun; every 1 second, the snake grows!
    if pygame.time.get_ticks() - start_time > 1000:
        start_time = pygame.time.get_ticks()
        my_snake.grow()

    ### Fill the screen with white! ###
    screen.fill("white")

    ### Some beginner game logic to update the snake every frame. ###  
    my_snake.update()
            
    pygame.display.update()  # Update the display