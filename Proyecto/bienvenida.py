import pygame
import variables


def mostrar_pantalla_inicio():
    pygame.init()
    pantalla = variables.screen
    fuente = pygame.font.Font("Proyecto//assets//fonts//PressStart2P-Regular.ttf", 18)
    fondo = pygame.image.load("Proyecto//assets//fondo1.png")  
    fondo = pygame.transform.scale(fondo, (variables.ancho, variables.alto))  
    boton_jugar = pygame.image.load("Proyecto//assets//boton_start.png")  
    boton_jugar = pygame.transform.scale(boton_jugar, (200, 100))  
    posicion_boton_jugar = boton_jugar.get_rect(topleft=(285, 320)) 
    caja_texto = pygame.Rect(220, 334, 350, 32)
    color_activo = pygame.Color('dodgerblue2')
    color = color_activo  
    activo = True 
    texto = ''
    placeholder = 'Ingresa tu apuesta'
    apuesta = 1
    capital = 30000
    terminado = False
    mensaje_error = ''

    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if posicion_boton_jugar.collidepoint(evento.pos):
                    if texto == '' or texto == placeholder:
                        mensaje_error = "Debes ingresar un monto válido."
                    else:
                        try:
                            apuesta = int(texto)
                            if 0 < apuesta <= capital:
                                terminado = True 
                            else:
                                mensaje_error = "No puedes apostar más de $30.000."
                        except ValueError:
                            mensaje_error = "Debes ingresar un monto válido."
                    texto = ''  
                    
            if evento.type == pygame.KEYDOWN:
                if activo:
                    if evento.key == pygame.K_BACKSPACE:
                        texto = texto[:-1]
                    else:
                        texto += evento.unicode

        pantalla.blit(fondo, (0, 0))

        if not texto:
            superficie_placeholder = fuente.render(placeholder, True, color) 
            pantalla.blit(superficie_placeholder, (230, caja_texto.y + 5))  
            pygame.draw.rect(pantalla, color, caja_texto, 2)
        else:
            superficie_texto = fuente.render(texto, True, color)
            pantalla.blit(superficie_texto, (caja_texto.x + 5, caja_texto.y + 5))  
            pygame.draw.rect(pantalla, color, caja_texto, 2)

        pantalla.blit(boton_jugar, posicion_boton_jugar.topleft)
        texto_capital = fuente.render(f"Capital: ${capital}", True, (255, 255, 255))
        pantalla.blit(texto_capital, (250, 300))

        if mensaje_error:
            texto_error = fuente.render(mensaje_error, True, (255, 0, 0))
            pantalla.blit(texto_error, (125, 106))

        pygame.display.flip()

    return apuesta  # Devolver la apuesta ingresada Devolver la apuesta ingresada