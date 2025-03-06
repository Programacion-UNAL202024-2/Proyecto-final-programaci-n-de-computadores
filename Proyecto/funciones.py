import math
import pygame
from bienvenida import mostrar_pantalla_inicio
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
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i+8],(322,320))
            variables.screen.blit(variables.frutas[i+5],(429,320))
        except IndexError:
            variables.screen.blit(variables.frutas[i],(215,320))
            variables.screen.blit(variables.frutas[i-2],(322,320))
            variables.screen.blit(variables.frutas[i-1],(429,320))

        pygame.display.flip()

def calcular_puntaje(fruta1, fruta2, fruta3):
    cereza = variables.frutas[4]
    cantidad_cerezas = sum(1 for simbolo in [fruta1, fruta2, fruta3] if simbolo == cereza)

    if cantidad_cerezas == 2:
        return 2
    elif cantidad_cerezas == 1:
        return 1

    if fruta1 == fruta2 == fruta3: 
        if fruta1 == variables.frutas[7]:  
            return 100
        elif fruta1 == variables.frutas[8]:  
            return 50
        elif fruta1 == variables.frutas[6]:  
            return 30
        elif fruta1 == variables.frutas[0]: 
            return 20
        elif fruta1 == variables.frutas[4]:  
            return 15
        elif fruta1 == variables.frutas[3]: 
            return 10
        elif fruta1 == variables.frutas[1]:  
            return 5
        elif fruta1 == variables.frutas[2]:  
            return 3
        
    return 0  

def calcular_probabilidad_jackpot(apuesta, k):
    return 1 - math.exp(-apuesta / k)

def start(n, apuesta):
    show_animation(n)
    numero_1 = random.randint(0, 8)
    numero_2 = random.randint(0, 8)
    numero_3 = random.randint(0, 8)

    probabilidad_jackpot = calcular_probabilidad_jackpot(apuesta, k=100000)

    if random.random() < probabilidad_jackpot:
        numero_1 = numero_2 = numero_3 = 7  # Jackpot

    variables.screen.blit(variables.frutas[numero_1], (215, 320))
    variables.screen.blit(variables.frutas[numero_2], (322, 320))
    variables.screen.blit(variables.frutas[numero_3], (429, 320))
    pygame.display.flip()
    
    puntaje = calcular_puntaje(variables.frutas[numero_1], variables.frutas[numero_2], variables.frutas[numero_3])
    ganancia = puntaje * apuesta
    return puntaje, ganancia, numero_1, numero_2,
    

def dividir_texto(texto, fuente, ancho_maximo):
    palabras = texto.split(' ')
    lineas = []
    linea_actual = ''
    
    for palabra in palabras:
        if fuente.size(linea_actual + palabra)[0] <= ancho_maximo:
            linea_actual += palabra + ' '
        else:
            lineas.append(linea_actual)
            linea_actual = palabra + ' '
    
    if linea_actual:
        lineas.append(linea_actual)
    
    return lineas

def mostrar_modal(mensaje):
    fondo_modal = pygame.image.load("Proyecto/assets/fondo2.png")
    fondo_modal = pygame.transform.scale(fondo_modal, (variables.ancho, variables.alto))

    modal = pygame.Surface((600, 400), pygame.SRCALPHA)
    modal.fill((0, 0, 0, 200))

    fuente = pygame.font.Font("Proyecto//assets//fonts//PressStart2P-Regular.ttf", 18)

    lineas = dividir_texto(mensaje, fuente, 550) 
    y_offset = 150  

    for linea in lineas:
        texto_mensaje = fuente.render(linea, True, (255, 255, 255))
        texto_rect = texto_mensaje.get_rect(center=(300, y_offset))
        modal.blit(texto_mensaje, texto_rect)
        y_offset += 30  

    texto_boton = fuente.render("Continuar", True, (255, 255, 255))
    boton_rect = texto_boton.get_rect(center=(300, y_offset + 40))  

    pygame.draw.rect(modal, (0, 0, 255), boton_rect.inflate(20, 10))  
    modal.blit(texto_boton, boton_rect) 


    variables.screen.blit(fondo_modal, (0, 0)) 
    variables.screen.blit(modal, (100, 100))
    pygame.display.flip()

    continuar = False
    while not continuar:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_clic = pygame.mouse.get_pos()
                posicion_clic_modal = (posicion_clic[0] - 100, posicion_clic[1] - 100)
                if boton_rect.collidepoint(posicion_clic_modal):
                    continuar = True

    return True  