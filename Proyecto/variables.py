import pygame

ancho = 800
alto = 600

screen = pygame.display.set_mode((ancho, alto))

frutas = []
for i in range(8):
    default = pygame.image.load(f"Proyecto//assets//fruticas//f_0{i}.png")
    new = pygame.transform.scale(default,(80,80))
    frutas.append(new)


