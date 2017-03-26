import pygame


class Bar(pygame.sprite.Sprite):
    IDLE, POSITIVE, NEGATIVE = range(3)

    def __init__(self, screen_size, max_speed):
        pygame.sprite.Sprite.__init__(self)
        self.screen_size = screen_size
        self.max_speed = max_speed
        self.acceleration_factor = 1.1
        self.acceleration = 1
        self.speed = 0
        self.status = Bar.IDLE
        self.last_key = pygame.K_UNKNOWN

    def on_update(self):
        self.check_boundary()
        if self.status == Bar.IDLE:
            self.speed = 0
            self.acceleration = 1
            self.last_key = pygame.K_UNKNOWN
        elif self.status == Bar.NEGATIVE:
            self.acceleration *= self.acceleration_factor
            self.speed = -min(self.max_speed, abs(self.speed - self.acceleration))
        elif self.status == Bar.POSITIVE:
            self.acceleration *= self.acceleration_factor
            self.speed = min(self.max_speed, self.speed + self.acceleration)

    def on_draw(self, surface):
        surface.blit(self.surface, self.rect)
