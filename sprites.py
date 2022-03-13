from pkgutil import ImpImporter
import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self,game,x,y):

        self.game = game
        self._layer = player_layer
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self,self.groups)

        self.x = x*tilesize
        self.y = y*tilesize
        self.width = tilesize
        self.height = tilesize

        self.image = pygame.Surface([self.width,self.height])
        self.image.fill(red)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        pass