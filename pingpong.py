# Algorithm
# Import pygame library.
import pygame

# Initialize pygame.
pygame.init()

display = pygame.display.set_mode((640, 640))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
