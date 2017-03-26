import pygame

from model.Bar import Bar
from model.BarHorizontal import BarHorizontal


class BarTop(BarHorizontal):
    def __init__(self, screen_size, max_speed):
        BarHorizontal.__init__(self, screen_size, max_speed)
        self.surface = pygame.image.load('imgs/bar_top.png')
        self.rect = self.surface.get_rect()
        self.init_position()

    def init_position(self):
        self.rect.left = (self.screen_size[0] - self.rect.width) / 2

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.status = Bar.NEGATIVE
                self.last_key = pygame.K_a
            if event.key == pygame.K_d:
                self.status = Bar.POSITIVE
                self.last_key = pygame.K_d
        elif event.type == pygame.KEYUP:
            if (self.last_key == pygame.K_a and event.key == pygame.K_a) or (
                            self.last_key == pygame.K_d and event.key == pygame.K_d):
                self.status = Bar.IDLE

    def check_boundary(self):
        if self.rect.left < self.rect.height:
            self.rect.left = self.rect.height
            self.status = Bar.IDLE
        if self.rect.right > self.screen_size[0] - self.rect.height:
            self.rect.right = self.screen_size[0] - self.rect.height
            self.status = Bar.IDLE

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            ball.speed[1] = abs(ball.speed[1])
