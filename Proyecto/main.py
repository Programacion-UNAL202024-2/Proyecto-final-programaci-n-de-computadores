import pygame
import variables
from funciones import start

pygame.init()
pygame.display.set_caption("Slot machine")
run = True

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start()
    pygame.display.update()
pygame.quit()











