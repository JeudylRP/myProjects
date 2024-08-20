'''
------- 1. Wir programmieren
------- 2. Ressourcen für das Spiel
------- 3. Das Modul pygame (Neue Obe..)
------- 4. Das Modul pygame (Alte Ober...)
------- 5. Das Spielfenster erzeugen
------- 6. Titel, Framerate und Hintergrund modifizi...
------- 7. Das Raumschiff platzieren
------- 8. Bewegung eingrenzen
------- 8. Geschoss implementieren
------- 10. ALiens Platzieren
------- 11. Kollision zwischen Alien und Geschoss erfassen
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

        self.enemies = []
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130))
            '''
            self.enemies.append(Enemy(self,random.randint(0,736), random.randint(0,130))
            1. self.enemies.append(...)
            - self.enemies: Das isi eine Liste, also wie eine Sammlung, in der wier Alle Aliens peichern.
            - append(...): Das bedeutet "hinzufügen". Hier fügern wir ein neues Alien zu dieser Liste hinzu.
            
            2.Enemy(self, random.randint(0,736), random.randint(0,130)
            
            - Enemy(...): Hier wird ein neues Alien erstellt.
            - self: Das bedeutet, dass dieses Alien zu dem Spiel gehört, das du geerade spielst.
            
            - random.rendint(0,736): Das wählt eine zufällige Zahl zwischen 0 und 736. Diese Zahl bestimmt, wie weit links oder rechts auf dem Bildschirm das Alien erscheinen Soll.
            
            - random.randint(0,130): Das wählt eine zufällige Zahl zwischen 0 und 130. Diese Zahl bestimmt, wie weit oben auf demm Bildschirm das Alien erscheinen soll.
            ---  Zusammengefasst: Dieser Code erstellt ein Alien an einem zufälligeb Ort oben auf dem Bildschirm und fügt es zu Liste alles Alliens hinzu, die im Spiel existieren.
            '''
            self.background_img = pygame.image.load("spr_space_himmel.png")
        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)
                    if event.key == pygame.KE
