import pygame as pg
from pygame.locals import *

WIDTH, HEIGHT = 400, 200
FPS = 24


class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Tekst")
        self.running = True
        self.all_sprites = pg.sprite.Group()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill("black")
        self.all_sprites.draw(self.screen)

        # Tekst
        text = "Game Over"
        font = pg.font.SysFont("Arial", 50)
        text_surface = font.render(text, True, "green")
        self.screen.blit(text_surface, (WIDTH/2-100, HEIGHT/2-25))

        pg.display.update()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pg.quit()


if __name__ == "__main__":
    app = App()
    app.run()

# Smidig IT-2 © TIP AS, 2024