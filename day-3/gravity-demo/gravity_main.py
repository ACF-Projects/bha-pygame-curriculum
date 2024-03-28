"""
We've covered drawing, moving, clocks, collisions,
and classes! Here is one example project: gravity.
"""

import pygame
import player

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

my_player = player.Player(screen)
platforms = [pygame.Rect(0, 400, screen.get_width(), 200)]

running = True

while running:

    clock.tick(60)
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### Fill the screen with a white background. ###
    screen.fill("white")

    ### Update the player's information every frame. ###
    my_player.update(platforms)

    ### Draw all platforms onto the screen. ###
    for platform in platforms:
        pygame.draw.rect(screen, "black", platform)
            
    pygame.display.update()  # Update the display