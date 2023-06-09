import pygame
import os
def main():
    ancho = 400
    alto = 400
    color = (255,255,255)
    lienzo = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Ventana 1")
    hecho = True
    while hecho:
        lienzo.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hecho = False
                os._exit(0)
        pygame.display.update()

if __name__=='__main__':
    pygame.init()
    main()