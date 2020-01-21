from pygame import *   #podemos usar la clase de pygame sin poner nada delante
#import pygame as pg   nos obliga a poner pg. delante de cada clase de pygame que vayamos a usar
from pygame.locals import * #contiene varias constantes como las teclas
import sys

#inicializamos pygame
init()

class Robot:
    speed = 5
    images = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.image = image.load('resources/robot_r01.png').convert_alpha()

    def go_up(self):
        #if self.y > 0:
        #   self.y -= self.speed
        self.y = max(0, self.y - self.speed) #self.y es el maximo entre self.y menos speed. Si self.y=100 va a ser el max entre 0 y 95, asi que sera 95. Si self.y=0 el max entre 0 y -5 es 0.

    def go_down(self):
        self.y = min(600, self.y + self.speed)

    def go_left(self):
        self.x = max(0, self.x - self.speed)

    def go_right(self):
        self.x = min(800, self.x + self.speed)

    @property
    def position(self):
        return self.x, self.y

#Creamos la pantalla
screen = display.set_mode((800, 600))
display.set_caption('Título de la pantalla')
background_color = (150, 150, 222)

robot = Robot(400, 300)

#Bucle básico
while True:
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            sys.exit()
        
        #Procesar el resto de eventos
        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                robot.go_up()
            if ev.key == K_DOWN:
                robot.go_down()
            if ev.key == K_LEFT:
                robot.go_left()
            if ev.key == K_RIGHT:
                robot.go_right()

    keys_pressed = key.get_pressed()
    if keys_pressed[K_UP]:
        robot.go_up()
    if keys_pressed[K_DOWN]:
        robot.go_down()
    if keys_pressed[K_LEFT]:
        robot.go_left()
    if keys_pressed[K_RIGHT]:
        robot.go_right()

    print(robot.position)

    screen.fill(background_color) #rellena la pantalla con el color de fondo
    screen.blit(robot.image, robot.position) #posiciona el robot en la pantalla

    display.flip() #refresca o redibuja

