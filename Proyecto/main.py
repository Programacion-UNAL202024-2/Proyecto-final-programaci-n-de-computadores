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
imagen_contador = pygame.transform.scale(imagen_contador, (300, 90)) 

puntaje = 0  
ganancia = 0  
resultado_frutas = None 

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if capital >= apuesta:  
                    puntaje, ganancia, numero_1, numero_2, numero_3 = start(8, apuesta) 
                    capital += ganancia - apuesta 
                    resultado_frutas = (
                        variables.frutas[numero_1],  
                        variables.frutas[numero_2], 
                        variables.frutas[numero_3]   
                    )
                else: 
                    mensaje = "¡No tienes suficiente dinero para realizar esta apuesta!" if capital > 0 else "¡Te quedaste sin dinero! Por favor, realiza una nueva apuesta."
                    continuar = mostrar_modal(mensaje)  
                    if continuar:
                        capital = 30000 
                        apuesta = mostrar_pantalla_inicio()  
                        if apuesta is None:
                            run = False  
            
    if run: 
        variables.screen.blit(fondo, (0, 0))  
        variables.screen.blit(variables.frame_maquina_escalado, (30, 20))  

        if resultado_frutas:
            variables.screen.blit(resultado_frutas[0], (215, 320))  
            variables.screen.blit(resultado_frutas[1], (322, 320))  
            variables.screen.blit(resultado_frutas[2], (429, 320)) 

        variables.screen.blit(imagen_contador, (500, 0)) 

        fuente = pygame.font.Font("Proyecto//assets//fonts//PressStart2P-Regular.ttf", 15)
        texto_puntaje = fuente.render(f"Puntaje: {puntaje}", True, (255, 255, 255)) 
        texto_ganancia = fuente.render(f"Ganancia: {ganancia}", True, (255, 255, 255)) 
        texto_capital = fuente.render(f"Capital: {capital}", True, (255, 255, 255))  

        variables.screen.blit(texto_puntaje, (510, 20)) 
        variables.screen.blit(texto_ganancia, (510, 50))  
        variables.screen.blit(texto_capital, (510, 85))  

        pygame.display.update()  
        clock.tick(30)  

pygame.quit()