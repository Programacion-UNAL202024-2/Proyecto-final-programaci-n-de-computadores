import pygame
import variables
pygame.init()
pygame.display.set_caption("Slot machine")
run = True
screen = pygame.display.set_mode((variables.ancho, variables.alto))
while run == True:
    screen.blit(variables.primera_imagen,(150,150))
    screen.blit(variables.segunda_imagen,(310,150))
    screen.blit(variables.tercera_imagen,(470,150))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()











