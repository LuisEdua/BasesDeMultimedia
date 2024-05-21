import pygame
import math

ancho_pantalla = 800
alto_pantalla = 600

# Crea una ventana de 800x600 píxeles
ventana = pygame.display.set_mode((ancho_pantalla, alto_pantalla))

# Establece el color de fondo
color_pantalla = (255, 255, 255)
color_dibujo = (0, 0, 0)

# Variable para controlar el primer clic
primer_click = False

circulos = []

ancho = 800
alto = 800

color = (255, 255, 255)
color_d = (0, 0, 0)

x1, x2, y1, y2 = 0, 0, 0, 0

def obtener_radio(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


while True:
    # Obtiene los eventos del usuario
    eventos = pygame.event.get()
    # Maneja los eventos
    for evento in eventos:
        if evento.type == pygame.QUIT or evento.type == pygame.K_ESCAPE:
            # Sale del bucle y termina el programa si se cierra la ventana
            pygame.quit()
            exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = evento.pos
            primer_click = True

        if evento.type == pygame.MOUSEMOTION:
            if primer_click:
                ventana.fill(color_pantalla)
                x2, y2 = evento.pos
                radio = obtener_radio(x1, y1, x2, y2)
                pygame.draw.circle(ventana, color_dibujo, (x1, y1), radio)
                pygame.draw.circle(ventana, color_pantalla, (x1, y1), 0.99*radio)

        if evento.type == pygame.MOUSEBUTTONUP:
            if primer_click:
                primer_click = False



    # Actualiza la ventana
    pygame.display.update()