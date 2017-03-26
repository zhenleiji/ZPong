import pygame

from model.Bar import Bar
from model.BarVertical import BarVertical


class BarRight(BarVertical):
    def __init__(self, screen_size, max_speed):
        BarVertical.__init__(self, screen_size, max_speed)
        self.surface = pygame.image.load('imgs/bar_right.png')
        self.rect = self.surface.get_rect()
        self.init_position()

    def init_position(self):
        self.rect.left = self.screen_size[0] - self.rect.width
        self.rect.top = (self.screen_size[1] - self.rect.height) / 2

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.status = Bar.NEGATIVE
                self.last_key = pygame.K_UP
            if event.key == pygame.K_DOWN:
                self.status = Bar.POSITIVE
                self.last_key = pygame.K_DOWN
        elif event.type == pygame.KEYUP:
            if (self.last_key == pygame.K_UP and event.key == pygame.K_UP) or (
                            self.last_key == pygame.K_DOWN and event.key == pygame.K_DOWN):
                self.status = Bar.IDLE

    def check_boundary(self):
        if self.rect.top < self.rect.width:
            self.rect.top = self.rect.width
            self.status = Bar.IDLE
        if self.rect.bottom > self.screen_size[1] - self.rect.width:
            self.rect.bottom = self.screen_size[1] - self.rect.width
            self.status = Bar.IDLE

    def check_collision(self, ball):
        if self.rect.colliderect(ball.rect):
            ball.speed[0] = -abs(ball.speed[0])
            ball.speed[1] += self.speed * 0.1
