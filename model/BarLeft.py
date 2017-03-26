import pygame

from model.Bar import Bar
from model.BarVertical import BarVertical


class BarLeft(BarVertical):
    def __init__(self, screen_size, max_speed):
        BarVertical.__init__(self, screen_size, max_speed)
        self.surface = pygame.image.load('imgs/bar_left.png')
        self.rect = self.surface.get_rect()
        self.init_position()

    def init_position(self):
        self.rect.top = (self.screen_size[1] - self.rect.height) / 2

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                self.status = Bar.NEGATIVE
                self.last_key = pygame.K_w
            if event.key == pygame.K_s:
                self.status = Bar.POSITIVE
                self.last_key = pygame.K_s
        elif event.type == pygame.KEYUP:
            if (self.last_key == pygame.K_w and event.key == pygame.K_w) or (
                            self.last_key == pygame.K_s and event.key == pygame.K_s):
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
            ball.speed[0] = abs(ball.speed[0])
            ball.speed[1] += self.speed * 0.1
