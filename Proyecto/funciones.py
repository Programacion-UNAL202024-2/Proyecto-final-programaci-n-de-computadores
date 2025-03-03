import pygame
import variables
import random


def show_animation(cuanto):
    for i in range (cuanto):
        pygame.time.delay(200)
        try:
            variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frame_1,(30,20)) 
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i+3],(322,320))
            variables.screen.blit(variables.frutas[i+5],(429,320))
        except IndexError:
            variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frame_1,(30,20)) 
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i-2],(322,320))
            variables.screen.blit(variables.frutas[i-1],(429,320))

        pygame.display.flip()



def start():
    numero_1 = random.randint(0,8)
    numero_2 = random.randint(0,8)
    numero_3 = random.randint(0,8)

    variables.screen.fill((255,255,255))
    variables.screen.blit(variables.frame_1,(30,20)) 
    variables.screen.blit(variables.frutas[numero_1],(215,320))
    variables.screen.blit(variables.frutas[numero_2],(322,320))
    variables.screen.blit(variables.frutas[numero_3],(429,320))




