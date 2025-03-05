import pygame
import variables

def mostrar_pantalla_inicio():
    pygame.init()
    pantalla = variables.screen
    fuente = pygame.font.Font("assets/fonts/PressStart2P-Regular.ttf", 36)
    fondo = pygame.image.load("Proyecto//assets//fondo1.png")  
    fondo = pygame.transform.scale(fondo, (variables.ancho, variables.alto))  
    boton_jugar = pygame.image.load("Proyecto//assets//boton_start.png")  
    boton_jugar = pygame.transform.scale(boton_jugar, (200, 50))  
    posicion_boton_jugar = boton_jugar.get_rect(topleft=(285, 350)) 
    caja_texto = pygame.Rect(285, 334, 200, 32)
    color_inactivo = pygame.Color('lightskyblue3')
    color_activo = pygame.Color('dodgerblue2')
    color = color_inactivo
    activo = False
    texto = ''
    apuesta = 0
    capital = 30000
    terminado = False
    mensaje_error = ''

    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if caja_texto.collidepoint(evento.pos):
                    activo = not activo
                else:
                    activo = False
                color = color_activo if activo else color_inactivo
                if posicion_boton_jugar.collidepoint(evento.pos):
                    try:
                        apuesta = int(texto)
                        if 0 <= apuesta <= capital:
                            terminado = True 
                        else:
                            mensaje_error = "Error: Apuesta inválida. Debe ser entre 0 y 30.000."
                            texto = ''
                    except ValueError:
                        mensaje_error = "Error: Ingrese un número válido."
                        texto = ''
            if evento.type == pygame.KEYDOWN:
                if activo:
                    if evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += evento.unicode

        pantalla.blit(fondo, (0, 0))

        superficie_texto = fuente.render(texto, True, color)
        ancho_caja = max(200, superficie_texto.get_width() + 10)
        caja_texto.w = ancho_caja
        pygame.draw.rect(pantalla, color, caja_texto, 2)
        pantalla.blit(superficie_texto, (caja_texto.x + 5, caja_texto.y + 5))

        pantalla.blit(boton_jugar, posicion_boton_jugar.topleft)
        texto_capital = fuente.render(f"Capital: {capital} pesos", True, (255, 255, 255))
        pantalla.blit(texto_capital, (260, 300))

        if mensaje_error:
            texto_error = fuente.render(mensaje_error, True, (255, 0, 0))
            pantalla.blit(texto_error, (250, 300))

        pygame.display.flip()

    return apuesta