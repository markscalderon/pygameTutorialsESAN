import pygame
import os
def main():
    ancho = 400
    alto = 400
    color = (255,255,255)
    red = (255,0,0)
    lienzo = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Ventana 1")
    hecho = True
    reloj = pygame.time.Clock()
    while hecho:
        lienzo.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hecho = False
        pygame.draw.rect(lienzo, red, [10,10,40,40], width=0)
        pygame.display.update()
        reloj.tick(20)

if __name__=='__main__':
    pygame.init()
    main()
    pygame.quit()