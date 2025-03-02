import pygame
import variables
pygame.init()
pygame.display.set_caption("Slot machine")
run = True
ventana = pygame.display.set_mode((variables.ancho, variables.alto))
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()











