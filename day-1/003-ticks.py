"""
Let's add a clock to make our movement more
streamlined for all computers!

Exercise: Make a local multiplayer game! Add another
          object that moves when the ARROW KEYS are
          pressed, separate from the WASD player.
"""

import pygame

# Initialize the game engine
pygame.init()

# Set the height and width of the screen
screen = pygame.display.set_mode((800, 600))
### Create a clock object! This will regulate how fast our game runs. ###
clock = pygame.time.Clock()

running = True

### Make our player position! This will be changed. ###
player_pos = [400, 300]

while running:
    # Check for events (ex: if the X button is pressed, stop)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ### Make our clock limit the amount of times our code can run! ###
    clock.tick(60)

    ### Fill the screen with white! ###
    screen.fill("white")
    ### Draw a circle at our position! ###  
    pygame.draw.circle(screen, "blue", (player_pos[0], player_pos[1]), 50)

    ### Returns a dictionary of keys pressed IN THIS FRAME! ###
    pressed_keys = pygame.key.get_pressed()
    ### Prints specific statements when WASD are pressed. ###
    if pressed_keys[pygame.K_w]:
        player_pos[1] -= 10
    if pressed_keys[pygame.K_a]:
        player_pos[0] -= 10
    if pressed_keys[pygame.K_s]:
        player_pos[1] += 10
    if pressed_keys[pygame.K_d]:
        player_pos[0] += 10
            
    pygame.display.update()  # Update the display