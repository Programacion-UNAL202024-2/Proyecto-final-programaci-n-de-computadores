import pygame
import variables
from funciones import *

pygame.init()
pygame.display.set_caption("Slot machine")
puntaje_total = 0
clock = pygame.time.Clock()
run = True



while run == True:
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                try:
                    puntaje = start(8)  
                    puntaje_total += puntaje  
                    print(f"Puntaje total: {puntaje_total}")  
                except Exception as e:
                        print(f"Error en el proceso de inicio: {e}")
                        run = False 
 
    pygame.display.update()  
    clock.tick(30) 
pygame.quit()











