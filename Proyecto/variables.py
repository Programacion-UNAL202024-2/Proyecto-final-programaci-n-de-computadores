import pygame

ancho = 800
alto = 600

screen = pygame.display.set_mode((ancho, alto))

frutas = []
for i in range(9):
    default = pygame.image.load(f"Proyecto//assets//fruticas//f_0{i}.png")
    new = pygame.transform.scale(default,(80,80))
    frutas.append(new)

sprite_default = pygame.image.load("Proyecto//assets//maquina1.png")



frame = sprite_default.subsurface(0,0,850,1080)
frame_1 = pygame.transform.scale(frame, (750,600))

