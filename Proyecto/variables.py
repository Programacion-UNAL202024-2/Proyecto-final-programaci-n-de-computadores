import pygame
import random

numero_1 = random.randint(0,7)
numero_2 = random.randint(0,7)
numero_3 = random.randint(0,7)
ancho = 800
alto = 600

#defino la imagen como un objeto
imagen1 = pygame.image.load(f"assets//fruticas//f_0{numero_1}.png")
primera_imagen = pygame.transform.scale(imagen1,(100,100))

imagen2 = pygame.image.load(f"assets//fruticas//f_0{numero_2}.png")
segunda_imagen = pygame.transform.scale(imagen2,(100,100))

imagen3 = pygame.image.load(f"assets//fruticas//f_0{numero_3}.png")
tercera_imagen = pygame.transform.scale(imagen3,(100,100))

