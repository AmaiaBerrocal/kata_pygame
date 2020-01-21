from pygame import *   #podemos usar la clase de pygame sin poner nada delante
#import pygame as pg   nos obliga a poner pg. delante de cada clase de pygame que vayamos a usar
from pygame.locals import * #contiene varias constantes como las teclas
import sys
from random import randint

#inicializamos pygame
init()
FPS = 60

class Bomb:
    pictures = ['bomb_01.png', 'bomb_02.png', 'bomb_03.png', 'bomb_04.png']
  
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
            
        self.frame_act = 0
        self.num_frames = len(self.frames)
        
        self.current_time = 0
        self.animation_time = FPS//4


    def update(self, dt):
        self.current_time += dt
        if self.current_time <= self.animation_time:
            self.frame_act += 1
            if self.frame_act == self.num_frames:
                self.frame_act = 0
    

    @property
    def position(self):
        return self.x, self.y

    @property
    def image(self):
        return self.frames[self.frame_act]


class Robot:
    speed = 5
    pictures = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
        #self.frames = [image.load('resources/{}'.format(pict)).convert_alpha() for pict in self.pictures]   es el mismo for que arriba
        
        self.frame_act = 0
        self.num_frames = len(self.frames)

    def change_frame(self):
        self.frame_act += 1
        if self.frame_act == self.num_frames:
            self.frame_act = 0
        #self.frame_act = (self.frame_act + 1) % self.num_frames  equivale a las 3 lineas de arriba. si frame_act=0, le voy a sumar 1. 1/4 el resto es 1. 2/4 resto 2, 3/4 resto 3, 4/4 resto 0: vuelve a posicion cero

    def go_up(self):
        #if self.y > 0:
        #   self.y -= self.speed
        self.y = max(0, self.y - self.speed) #self.y es el maximo entre self.y menos speed. Si self.y=100 va a ser el max entre 0 y 95, asi que sera 95. Si self.y=0 el max entre 0 y -5 es 0.
        self.change_frame()

    def go_down(self):
        self.y = min(600, self.y + self.speed)
        self.change_frame()

    def go_left(self):
        self.x = max(0, self.x - self.speed)
        self.change_frame()

    def go_right(self):
        self.x = min(800, self.x + self.speed)
        self.change_frame()

    @property
    def position(self):
        return self.x, self.y

    @property
    def image(self):
        return self.frames[self.frame_act]

class Game:
    clock = time.Clock()
    
    def __init__(self):
        self.screen = display.set_mode((800, 600))
        display.set_caption('Título de la pantalla')

        self.background_color = (150, 150, 222)

        self.robot = Robot(400, 300)

        self.bombas = []
        for i in range(5):
            self.bomb = Bomb(randint(0,750), randint(0,550))
            self.bombas.append(self.bomb)

    def gameOver(self):
        quit()
        sys.exit()
    
    def handleEvents(self):
        for ev in event.get():
            if ev.type == QUIT:
                self.gameOver()
                  
            if ev.type == KEYDOWN:
                if ev.key == K_UP:
                    self.robot.go_up()
                if ev.key == K_DOWN:
                    self.robot.go_down()
                if ev.key == K_LEFT:
                    self.robot.go_left()
                if ev.key == K_RIGHT:
                    self.robot.go_right()

        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP]:
            self.robot.go_up()
        if keys_pressed[K_DOWN]:
            self.robot.go_down()
        if keys_pressed[K_LEFT]:
            self.robot.go_left()
        if keys_pressed[K_RIGHT]:
            self.robot.go_right()

    
    def mainloop(self):
        while True:
            dt = self.clock.tick(FPS)
            
            self.handleEvents()
                            
            self.screen.fill(self.background_color) #rellena la pantalla con el color de fondo
            self.screen.blit(self.robot.image, self.robot.position) #posiciona el robot en la pantalla
            for b in self.bombas:
                b.update(dt)
                self.screen.blit(b.image, b.position)

            display.flip() #refresca o redibuja

if __name__ == '__main__':
    game = Game()
    game.mainloop()



