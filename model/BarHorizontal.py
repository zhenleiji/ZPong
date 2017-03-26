import pygame

from model.Bar import Bar


class BarHorizontal(Bar):
    def __init__(self, screen_size, max_speed):
        Bar.__init__(self, screen_size, max_speed)

    def on_update(self):
        Bar.on_update(self)
        self.rect = self.rect.move([self.speed, 0])
