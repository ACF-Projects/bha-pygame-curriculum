"""
Welcome to Pygame! This is a template you can use
to start building your own projects. This code
creates a basic functional Pygame game.

Author: <YOUR NAME HERE>
Grade Level: <YOUR GRADE LEVEL HERE>
"""

import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))

running = True

while running:
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### You would write your game logic in here! ###  
            
    pygame.display.update()  # Update the display