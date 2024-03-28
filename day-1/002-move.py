"""
Let's move our objects around by making the (x, y) 
coordinates change!

Exercise: Complete the code below to make the circle move!
"""

import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))

running = True

### Make our player position! This will be changed. ###
player_pos = [400, 300]

while running:
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### Fill the screen with white! ###
    screen.fill("white")
    ### Draw a circle at our position! ###  
    pygame.draw.circle(screen, "blue", (player_pos[0], player_pos[1]), 50)

    ### Returns a dictionary of keys pressed IN THIS FRAME! ###
    pressed_keys = pygame.key.get_pressed()
    ### Prints specific statements when WASD are pressed. ###
    if pressed_keys[pygame.K_w]:
        print("The W key is pressed!")
    if pressed_keys[pygame.K_a]:
        print("The A key is pressed!")
    if pressed_keys[pygame.K_s]:
        print("The S key is pressed!")
    if pressed_keys[pygame.K_d]:
        print("The D key is pressed!")
            
    pygame.display.update()  # Update the display