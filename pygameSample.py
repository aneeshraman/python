import pygame

pygame.init()
display = pygame.display.set_mode((100, 70), pygame.RESIZABLE)
pygame.display.set_caption("Sample", "Nochu")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
