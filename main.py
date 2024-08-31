import pygame
import constantes
from constantes import ESCALA_PERSONAJE
from personaje import Personaje

pygame.init()

ventana = pygame.display.set_mode((constantes.ANCHO_VENTANA,constantes.ALTO_VENTANA))

pygame.display.set_caption("Jueguito")

player_image = pygame.image.load("assets//images//characters//player//perrito.jpg")
player_image = pygame.transform.scale(player_image, (player_image.get_width()*constantes.ESCALA_PERSONAJE,player_image.get_height()*constantes.ESCALA_PERSONAJE))
jugador = Personaje(50,50, player_image)

#definir variables de movimiento del jugador
mover_arriba = False
mover_abajo = False
mover_izquierda = False
mover_derecha = False

#controlar el frame rate
reloj = pygame.time.Clock()

run = True
while run == True:

    #QUE VAYA A 60 FPS
    reloj.tick(constantes.FPS)


    ventana.fill(constantes.COLOR_BG)

    #Calcular movimiento de jugador
    delta_x = 0
    delta_y = 0

    if mover_derecha == True:
        delta_x = constantes.VELOCIDAD
    if mover_izquierda == True:
        delta_x = -constantes.VELOCIDAD
    if mover_arriba == True:
        delta_y = -constantes.VELOCIDAD
    if mover_abajo == True:
        delta_y = constantes.VELOCIDAD

    #mover al jugador

    jugador.movimiento(delta_x, delta_y)

    jugador.draw(ventana)

    for event in pygame.event.get():
        #Para cerrar el juego
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                mover_izquierda = True
            if event.key == pygame.K_d:
                mover_derecha = True
            if event.key == pygame.K_w:
                mover_arriba = True
            if event.key == pygame.K_s:
                mover_abajo = True

        #Para cuando se suelta la tecla
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                mover_izquierda = False
            if event.key == pygame.K_d:
                mover_derecha = False
            if event.key == pygame.K_w:
                mover_arriba = False
            if event.key == pygame.K_s:
                mover_abajo = False

    pygame.display.update()
pygame.quit()
