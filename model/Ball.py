import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, screen_size, position, speed):
        pygame.sprite.Sprite.__init__(self)
        self.surface = pygame.image.load('imgs/ball.png')
        self.screen_size = screen_size
        self.rect = self.surface.get_rect()
        self.rect.left = position[0]
        self.rect.top = position[1]
        self.speed = speed
        self.default_position = position
        self.default_speed = [speed[0], speed[1]]

    def check_boundary(self):
        return self.rect.left < 0 or self.rect.right > self.screen_size[0] or self.rect.top < 0 or self.rect.bottom > \
                                                                                                   self.screen_size[1]

    def on_update(self):
        self.rect = self.rect.move(self.speed)
        if self.check_boundary():
            self.rect.left = self.default_position[0]
            self.rect.top = self.default_position[1]
            self.speed = [self.default_speed[0], self.default_speed[1]]

    def on_draw(self, surface):
        surface.blit(self.surface, self.rect)
