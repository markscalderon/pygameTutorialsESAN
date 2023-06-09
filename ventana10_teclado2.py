import pygame
from math import pi
def main():
    ancho = 400
    alto = 400
    color = (255,255,255)
    VERDE = (0,255,0)
    NEGRO = (0,0,0)
    ROJO = (255,0,0)
    AZUL = (0,0,255)
    lienzo = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Ventana 1")
    hecho = True
    reloj = pygame.time.Clock()
    fuente = pygame.font.Font(None,25)
    ox, oy = 10,10
    dx, dy = 0,0
    while hecho:
        lienzo.fill(color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                hecho = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] :
            dx -= 3
        elif keys[pygame.K_RIGHT]:
            dx += 3
        elif keys[pygame.K_UP]:
            dy -= 3
        elif keys[pygame.K_DOWN]:
            dy += 3

        pygame.draw.rect(lienzo, ROJO, [10+dx, 10+dy, 40, 40], width=0)
        pygame.display.update()
        reloj.tick(20)

if __name__=='__main__':
    pygame.init()
    main()
    pygame.quit()