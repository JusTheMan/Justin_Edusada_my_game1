#File create by: Justin Edusada

import pygame as pg

from pygame.sprite import Sprite

from setting import * 

vec = pg.math.Vector2 

# create a player 

class Player(Sprite): 
    def __inite__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50,50))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.pos = vec (WIDTH/2, HEIGHT/2)
        self.vel = vec (0,0)
        self.acc = vec (0,0)
        self.cofric = 0.1 
        self.canjump = False 
    def input (self):
        keystate = pg.key.get_pressed
        
        if keystate[pg.K_a]: 
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_a]: 
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_a]: 
            self.acc.x = -PLAYER_ACC
        if keystate[pg.K_a]: 
            self.acc.x = -PLAYER_ACC
    def update(self): 
        self.acc =self.vel * PLAYER_FRICTION
        self.input()
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.center = self.pos

        
        
    

