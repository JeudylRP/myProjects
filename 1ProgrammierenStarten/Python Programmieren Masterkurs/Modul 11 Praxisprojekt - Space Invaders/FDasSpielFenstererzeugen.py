'''
------- 1. Einführung wir proraammieeren space Invaders!
------- 2. Ressourcen für das Spiel
------- 3. Das Modul pygame installieren (Neue Oberfläche)
------- 4. Das modul pygame installieren (Alte Oberfläche)
------- 5. Das Spielfenster erzeugen
------- 6. Titel, Framerate und Hintergrund modifizieren
------- 7. Das Raumschiff platzieren
------- 8. Bewegungsmechaniken implementieren
------- 9. Bewegung eingrenzen
------- 10. Geschoss implementieren
------- 11. Aliens platzieren
------- 12. Kollision zwischen Alien und Geschoss erfassen WIEDERHOLEN
------- 13.
------- 14.
'''

import pygame
import random


class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self, 370, 515)

        self.emnemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))
        self.background_img = pygame.image.load("spr_space_himmel.png")

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit() #Richtiges Beenden von Pygame ----------------------------
