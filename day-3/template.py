"""
We've covered drawing, moving, clocks, collisions,
and classes! You'll be looking at a variety of
different projects today. Here's a template to
get started on any of them, or make your own!

Author: <YOUR NAME HERE>
Grade Level: <YOUR GRADE LEVEL HERE>
"""

import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

running = True

while running:

    clock.tick(60)
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### You would write your game logic in here! ###  
            
    pygame.display.update()  # Update the display