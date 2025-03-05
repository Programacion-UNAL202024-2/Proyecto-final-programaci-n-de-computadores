import pygame
from variables import *
from funciones import *
from bienvenida import mostrar_pantalla_inicio

pygame.init()
pygame.display.set_caption("Slot machine")
puntaje_total = 0
capital = 30000
clock = pygame.time.Clock()
ganancia = 0
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
 
    variables.screen.fill((30, 30, 30)) 
    fuente = pygame.font.Font(None, 36)
    texto_puntaje = fuente.render(f"Puntaje: {puntaje_total}", True, (255, 255, 255))
    texto_ganancia = fuente.render(f"Ganancia: {ganancia}", True, (255, 255, 255))
    texto_capital = fuente.render(f"Capital: {capital}", True, (255, 255, 255))
    variables.screen.blit(texto_puntaje, (10, 10))
    variables.screen.blit(texto_ganancia, (10, 50))

    pygame.display.update()  
    clock.tick(30)  
pygame.quit()











