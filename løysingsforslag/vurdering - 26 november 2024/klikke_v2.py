import pygame as pg
from pygame.locals import *
from random import randint, choice

WIDTH, HEIGHT = 400, 600
FPS = 24
TID_PER_RUNDE = 10000  # Endre denne for å endre tiden du gir brukeren på å klikke
TID_NY_PLASSERING = 2000  # Denne bestemmer hvor ofte en firkant tegnes på en tilfeldig plass på spillbrettet
FIRKANT_STORRELSE = 50  # Størrelsen på firkanten

class App:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Klikke i vinkel!")
        self.running = True
        self.all_sprites = pg.sprite.Group()
        self.timer = pg.time.get_ticks()  # Denne skal brukes i sammenheng med å restarte spillet så ofte som TID_PER_RUNDE tilsier
        self.fargeliste = ["blue", "red", "green", "pink", "purple", "brown"]  # For å kunne endre bakgrunnsfargen underveis
        self.background_color = self.fargeliste[3]  # Startfarge
        self.antall_klikk = 0  # Teller for antall klikk
        self.siste_firkant_tid = pg.time.get_ticks()  # Tidspunktet for siste firkant
        self.firkant_posisjon = (0, 0)  # Startposisjon for firkanten

        try:
            with open("rekord-v2.txt", "r") as file:
                self.antall_klikk_rekord = int(file.read())
        except FileNotFoundError:  # Dersom vi ikke finner rekord-v2.txt, ..
            self.antall_klikk_rekord = 0

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                # Sjekk om klikket er innenfor firkanten
                if self.is_click_inside_firkant(event.pos):
                    self.antall_klikk += 1
                    print(f"Antall klikk: {self.antall_klikk}")

    def is_click_inside_firkant(self, pos):
        x, y = pos
        fx, fy = self.firkant_posisjon
        return fx <= x <= fx + FIRKANT_STORRELSE and fy <= y <= fy + FIRKANT_STORRELSE

    def update(self):
        self.all_sprites.update()

        if pg.time.get_ticks() - self.timer > TID_PER_RUNDE:
            print(f"Det har gått {TID_PER_RUNDE / 1000} sekunder, runden er ferdig!")
            fargeNy = choice(self.fargeliste)
            while self.background_color == fargeNy:
                fargeNy = choice(self.fargeliste)
            self.background_color = fargeNy

            if self.antall_klikk > self.antall_klikk_rekord:
                self.antall_klikk_rekord = self.antall_klikk
            print(f"Rekord: {self.antall_klikk_rekord}")

            self.antall_klikk = 0
            self.timer = pg.time.get_ticks()

        # Tegn en firkant på en tilfeldig plass så ofte som TID_NY_PLASSERING tilsier
        if pg.time.get_ticks() - self.siste_firkant_tid > TID_NY_PLASSERING:
            self.firkant_posisjon = (randint(0, WIDTH - FIRKANT_STORRELSE), randint(0, HEIGHT - FIRKANT_STORRELSE))
            self.siste_firkant_tid = pg.time.get_ticks()

    def draw(self):
        self.screen.fill(self.background_color)  # Setter den nye fargen som blir valgt i update-funksjonen

        self.all_sprites.draw(self.screen)

        # Tegn firkanten
        pg.draw.rect(self.screen, pg.Color("black"), (*self.firkant_posisjon, FIRKANT_STORRELSE, FIRKANT_STORRELSE))

        # Vis antall klikk i pågående runde i spillvinduet (NB: ikke en del av oppgaveteksten)
        font = pg.font.Font(None, 36)
        text = font.render(f"Klikk: {self.antall_klikk}", True, pg.Color("white"))
        self.screen.blit(text, (10, 10))

        pg.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

            # Når programmet er ferdig (brukeren lukker vindu), skrives rekorden til en tekstfil
            if self.antall_klikk_rekord > 0:
                with open("rekord-v2.txt", "w") as file:
                    file.write(str(self.antall_klikk_rekord))
        pg.quit()

if __name__ == "__main__":
    app = App()
    app.run()