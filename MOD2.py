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

lineas = []

ancho = 800
alto = 800

color = (255, 255, 255)
color_d = (0, 0, 0)

x1, x2, y1, y2 = 0, 0, 0, 0


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
            x2, y2 = x1, y1
            inicio = (x1, y1)
            final = (x2, y2)
            linea = {'inicio': inicio, 'final': final}
            lineas.append(linea)
            primer_click = True

        if evento.type == pygame.MOUSEMOTION:
            if primer_click:
                x1, y1 = x2, y2
                x2, y2 = evento.pos
                ventana.fill(color_pantalla)
                inicio = (x1, y1)
                final = (x2, y2)
                linea = {'inicio': inicio, 'final':final}
                lineas.append(linea)
                for line in lineas:
                    pygame.draw.line(ventana, color_dibujo, line.get('inicio'), line.get('final'))

        if evento.type == pygame.MOUSEBUTTONUP:
            if primer_click:
                primer_click = False



    # Actualiza la ventana
    pygame.display.update()
