import pygame
import variables
import random


def show_animation(cuanto):
    for i in range (cuanto):
        pygame.time.delay(400)
        try:
            variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frutas[i],(240,200))
            variables.screen.blit(variables.frutas[i+3],(360,200))
            variables.screen.blit(variables.frutas[i+5],(460,200))
        except IndexError:
            variables.screen.fill((255,255,255))
            variables.screen.blit(variables.frutas[i],(240,200))
            variables.screen.blit(variables.frutas[i-2],(360,200))
            variables.screen.blit(variables.frutas[i-3],(460,200))

        pygame.display.flip()

def start():
    numero_1 = random.randint(0,7)
    numero_2 = random.randint(0,7)
    numero_3 = random.randint(0,7)

    variables.screen.fill((255,255,255))
    variables.screen.blit(variables.frutas[numero_1],(240,200))
    variables.screen.blit(variables.frutas[numero_2],(360,200))
    variables.screen.blit(variables.frutas[numero_3],(460,200))




