import pygame
import variables
import random


def start():
    
    numero_1 = random.randint(0,7)
    numero_2 = random.randint(0,7)
    numero_3 = random.randint(0,7)

    variables.screen.fill((255,255,255))
    variables.screen.blit(variables.frutas[numero_1],(240,200))
    variables.screen.blit(variables.frutas[numero_2],(360,200))
    variables.screen.blit(variables.frutas[numero_3],(460,200))




