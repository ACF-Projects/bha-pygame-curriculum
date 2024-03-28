import pygame

pygame.init()

message = "Welcome to your first Pygame window!"
message_2 = "My name is LUCAS."

screen = pygame.display.set_mode((500, 500))
font = pygame.font.Font("freesansbold.ttf", 26)
text = font.render(message, True, "green", "blue")
text2 = font.render(message_2, True, "green", "red")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(text, ((500 - text.get_width()) / 2, 200))
    screen.blit(text2, ((500 - text2.get_width()) / 2, 250))
    
    pygame.display.update()