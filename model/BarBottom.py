import pygame

from model.Bar import Bar
from model.BarHorizontal import BarHorizontal


class BarBottom(BarHorizontal):
    def __init__(self, screen_size, max_speed):
        BarHorizontal.__init__(self, screen_size, max_speed)
        self.surface = pygame.image.load('imgs/bar_bottom.png')
        self.rect = self.surface.get_rect()
        self.init_position()

    def init_position(self):
        self.rect.left = (self.screen_size[0] - self.rect.width) / 2
        self.rect.top = self.screen_size[1] - self.rect.height

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.status = Bar.NEGATIVE
                self.last_key = pygame.K_LEFT
            if event.key == pygame.K_RIGHT:
                self.status = Bar.POSITIVE
                self.last_key = pygame.K_RIGHT
        elif event.type == pygame.KEYUP:
            if (self.last_key == pygame.K_LEFT and event.key == pygame.K_LEFT) or (
                            self.last_key == pygame.K_RIGHT and event.key == pygame.K_RIGHT):
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
            ball.speed[1] = -abs(ball.speed[1])
            ball.speed[0] += 0.1 * self.speed
