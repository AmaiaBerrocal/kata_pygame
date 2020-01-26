from pygame import * 
from pygame.locals import *

FPS = 60

class Bomb(sprite.Sprite):
    pictures = ['bomb_01.png', 'bomb_02.png', 'bomb_03.png', 'bomb_04.png']
    w = 44
    h = 42

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self)
        self.rect = Rect(self.x, self.y, self.w, self.h)
        
        self.frames = []
        for pict in self.pictures:
            frame = image.load('resources/{}'.format(pict)).convert_alpha()
            self.frames.append(frame)
            
        self.frame_act = 0
        self.num_frames = len(self.frames)
        
        self.current_time = 0
        self.animation_time = FPS//60

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.frame_act += 1
            if self.frame_act == self.num_frames:
                self.frame_act = 0
    
    @property
    def image(self):
        return self.frames[self.frame_act]


class Robot(sprite.Sprite):
    speed = 5
    pictures = ['robot_r01.png', 'robot_r02.png', 'robot_r03.png', 'robot_r04.png']
    w = 64
    h = 68
    lives = 3

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

        sprite.Sprite.__init__(self)
        self.rect = Rect(self.x, self.y, self.w, self.h)
         
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
        self.rect.y = max(0, self.rect.y - self.speed) #self.y es el maximo entre self.y menos speed. Si self.y=100 va a ser el max entre 0 y 95, asi que sera 95. Si self.y=0 el max entre 0 y -5 es 0.
        self.change_frame()

    def go_down(self):
        self.rect.y = min(600, self.rect.y + self.speed)
        self.change_frame()

    def go_left(self):
        self.rect.x = max(0, self.rect.x - self.speed)
        self.change_frame()

    def go_right(self):
        self.rect.x = min(800, self.rect.x + self.speed)
        self.change_frame()

    def comprobarToques(self, group):
        colisiones = sprite.spritecollide(self, group, True)
        for b in colisiones:
            self.lives -= 1
            self.rect.x = self.x #volvemos a la posicion de inicio
            self.rect.y = self.y
        return self.lives #desde aqui no podemos llamar a gameOver porque esta en Game, por eso devolvemos el numero de vidas

    @property
    def image(self):
        return self.frames[self.frame_act]
