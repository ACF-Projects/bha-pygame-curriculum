"""
Now, we'll learn about how to draw images
into our Pygame window!

Exercise: Draw the image of a flag onto the screen!
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

    ### Fill the screen with white! ###
    screen.fill("white")
    ### Draw a circle! ###  
    pygame.draw.circle(screen, "red", (500, 300), 50)
    ### Draw a square! ###  
    pygame.draw.rect(screen, "blue", (250, 250, 100, 100))
            
    pygame.display.update()  # Update the display