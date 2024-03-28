import pygame 

pygame.init() 

canvas = pygame.display.set_mode((400, 400)) 

running = True

apple_image = pygame.image.load('apple.png')
apple_image = pygame.transform.scale(apple_image, (400, 400))

while running: 
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT: 
      running = False
  
  canvas.blit(apple_image, (0, 0))
  
  pygame.display.update() 