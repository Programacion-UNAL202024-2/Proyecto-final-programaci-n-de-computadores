import pygame
from variables import *
from funciones import *
from bienvenida import mostrar_pantalla_inicio

pygame.init()
pygame.display.set_caption("Slot machine")
capital = 30000
clock = pygame.time.Clock()
run = True
apuesta = mostrar_pantalla_inicio()

if apuesta is None:
    run = False

fondo = pygame.image.load("Proyecto/assets/fondo2.png")
fondo = pygame.transform.scale(fondo, (800, 600))  

imagen_contador = pygame.image.load("Proyecto/assets/contador_puntaje.png")
imagen_contador = pygame.transform.scale(imagen_contador, (300, 110)) 

puntaje = 0  # Inicializar puntaje
ganancia = 0  # Inicializar ganancia

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if capital >= apuesta:  
                    puntaje, ganancia = start(8, apuesta) 
                    capital += ganancia - apuesta  
                else: 
                    mensaje = "¡No tienes suficiente dinero para realizar esta apuesta!" if capital > 0 else "¡Te quedaste sin dinero! Por favor, realiza una nueva apuesta."
                    continuar = mostrar_modal(mensaje) 
                    if continuar:
                        capital = 30000
                        apuesta = mostrar_pantalla_inicio()  # Volver a la pantalla de bienvenida
                        if apuesta is None:
                            run = False
            
    if run: 
        variables.screen.blit(fondo, (0, 0))  
        variables.screen.blit(imagen_contador, (500, 0)) 

        fuente = pygame.font.Font("Proyecto//assets//fonts//PressStart2P-Regular.ttf", 15)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255)) 
        texto_ganancia = fuente.render(f"Ganancia: {ganancia}", True, (255, 255, 255)) 
        texto_capital = fuente.render(f"Capital: {capital}", True, (255, 255, 255))  

        variables.screen.blit(texto_puntaje, (510, 13)) 
        variables.screen.blit(texto_ganancia, (510, 43))  
        variables.screen.blit(texto_capital, (510, 73))  
        pygame.display.update()  
        clock.tick(30)  

pygame.quit()