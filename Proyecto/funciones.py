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



def start(n):
    show_animation(n)
    numero_1 = random.randint(0,8)
    numero_2 = random.randint(0,8)
    numero_3 = random.randint(0,8)

    variables.screen.fill((255,255,255))
    animacion_maquina() 
    variables.screen.blit(variables.frutas[numero_1],(215,320))
    variables.screen.blit(variables.frutas[numero_2],(322,320))
    variables.screen.blit(variables.frutas[numero_3],(429,320))
    pygame.display.flip()




