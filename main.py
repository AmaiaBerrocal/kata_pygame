from pygame import *   #podemos usar la clase de pygame sin poner nada delante
#import pygame as pg   nos obliga a poner pg. delante de cada clase de pygame que vayamos a usar
from pygame.locals import * #contiene varias constantes como las teclas
import sys

#inicializamos pygame
init()

#Creamos la pantalla
screen = display.set_mode((800, 600))
display.set_caption('Título de la pantalla')
background_color = (150, 150, 222)

#Bucle básico
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        
        #Procesar el resto de eventos
        screen.fill(background_color) #rellena la pantalla con el color de fondo

        display.flip() #refresca o redibuja
        
