import pygame
import variables
import random

def animacion_maquina():
    for i in range(4):
        pygame.time.delay(20)
        frame = variables.sprite_default.subsurface(900 * i, 0, 900,1080)
        frame_escalado = pygame.transform.scale(frame, (800,600))
        variables.screen.blit(frame_escalado,(30,20))
        pygame.display.flip()

def show_animation(cuanto):
    for i in range (cuanto):
        pygame.time.delay(50)
        try:
            animacion_maquina()
   #         variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i+8],(322,320))
            variables.screen.blit(variables.frutas[i+5],(429,320))
        except IndexError:
  #          variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i-2],(322,320))
            variables.screen.blit(variables.frutas[i-1],(429,320))

        pygame.display.flip()

def calcular_puntaje(fruta1, fruta2, fruta3):
    cereza = variables.frutas[4]
    cantidad_cerezas = sum(1 for simbolo in [fruta1, fruta2, fruta3] if simbolo == cereza)

    if cantidad_cerezas == 2:
        return 2
    elif cantidad_cerezas == 1:
        return 1

    if fruta1 == fruta2 == fruta3: 
        if fruta1 == variables.frutas[7]:  
            return 100
        elif fruta1 == variables.frutas[8]:  
            return 50
        elif fruta1 == variables.frutas[6]:  
            return 30
        elif fruta1 == variables.frutas[0]: 
            return 20
        elif fruta1 == variables.frutas[4]:  
            return 15
        elif fruta1 == variables.frutas[3]: 
            return 10
        elif fruta1 == variables.frutas[1]:  
            return 5
        elif fruta1 == variables.frutas[2]:  
            return 3
        
    return 0  
   

def start(n, apuesta ):
    show_animation(n)
    numero_1 = random.randint(0,8)
    numero_2 = random.randint(0,8)
    numero_3 = random.randint(0,8)

    probabilidad_jackpot = min(apuesta / 50000, 1.0)
    if random.random() < probabilidad_jackpot:
        numero_1 = numero_2 = numero_3 = 7 

    variables.screen.fill((255,255,255))
    animacion_maquina() 
    variables.screen.blit(variables.frutas[numero_1],(215,320))
    variables.screen.blit(variables.frutas[numero_2],(322,320))
    variables.screen.blit(variables.frutas[numero_3],(429,320))
    pygame.display.flip()

    puntos = calcular_puntaje(variables.frutas[numero_1], variables.frutas[numero_2], variables.frutas[numero_3])

    return puntos 




