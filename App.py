import pygame
from model.Ball import Ball
from model.BarRight import BarRight
from model.BarLeft import BarLeft
from model.BarTop import BarTop
from model.BarBottom import BarBottom


class App:
    def __init__(self):
        # Initialise pygame
        self._running = True
        self._display_surf = None
        self.size_screen = self.weight, self.height = 1024, 764
        self.clock = pygame.time.Clock()
        self.background = 255, 255, 255

        # Initialise objects
        self.bars = [BarLeft(self.size_screen, 50), BarRight(self.size_screen, 50), BarTop(self.size_screen, 50),
                     BarBottom(self.size_screen, 50)]
        self.ball = Ball(self.size_screen, [self.weight / 2, self.height / 2], [10, 10])

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size_screen, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        for bar in self.bars:
            bar.on_event(event)

        if event.type == pygame.QUIT:
            self._running = False

    def on_cleanup(self):
        pygame.quit()

    def on_update(self):
        for bar in self.bars:
            bar.check_collision(self.ball)
            bar.on_update()

        self.ball.on_update()

    def on_draw(self):
        self._display_surf.fill(self.background)

        for bar in self.bars:
            bar.on_draw(self._display_surf)

        self.ball.on_draw(self._display_surf)

        pygame.display.flip()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while (self._running):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_update()
            self.on_draw()
            self.clock.tick(30)
        self.on_cleanup()
