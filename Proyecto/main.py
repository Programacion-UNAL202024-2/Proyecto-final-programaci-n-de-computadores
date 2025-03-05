import pygame
from variables import *
from funciones import *
from bienvenida import mostrar_pantalla_inicio

pygame.init()
pygame.display.set_caption("Slot machine")
puntaje_total = 0
capital = 30000
clock = pygame.time.Clock()
run = True
apuesta = mostrar_pantalla_inicio()

if apuesta is None:
    run = False

while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                try:
                    if capital >= apuesta:  
                        puntaje = start(8, apuesta) 
                        ganancia = puntaje * apuesta / 100  
                        capital += ganancia - apuesta  
                        puntaje_total += puntaje 
                        print(f"Puntaje total: {puntaje_total}")
                        print(f"Ganancia: {ganancia}")
                        print(f"Capital actual: {capital}")
                    else:
                        print("Error: No tienes suficiente capital para apostar.")
                except Exception as error:
                    print(f"Error en el proceso de inicio: {error}")
                    ejecutando = False
 
    pygame.display.update()  
    clock.tick(30) 
pygame.quit()











