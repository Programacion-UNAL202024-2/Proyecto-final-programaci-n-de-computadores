import pygame
pygame.init()

def extraer_sprite(hoja, frame, ancho, alto):
    sprite = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    sprite.blit(hoja, (0,0), (frame * ancho, 0, ancho, alto))
    return sprite





