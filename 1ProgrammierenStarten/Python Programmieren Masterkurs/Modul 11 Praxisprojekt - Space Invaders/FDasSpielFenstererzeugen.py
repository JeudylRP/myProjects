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
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()  # Richtiges Beenden von Pygame ----------------------------

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.spaceship.move(0)

            self.spaceship.update()

            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:
                        bullet.update()
                        # Kollision zwischen Schuss und Aliens prüfen
                        for enemy in self.enemies:
                            if bullet.check_collision(enemy):
                                self.enemies.remove(enemy)  # Entfernt das getroffen Alien
                                self.spaceship.bullets.remove(bullet)  # Entfernt den Schuss
                                break  # Verhindert Probleme bei der Iteration über die Liste

            for enemy in self.enemies:
                enemy.update()

            pygame.update()

            pygame.display.update()


class Spaceship:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship.png")
        self.bullets = []

    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))
        self.bullets[len(self.bullets) - 1].fire()

    def move(self, speed):
        self.change_x = speed

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))


class Bullet:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.is_fired = False
        self.bullet_speed = 10
        self.bullet_img = pygame.image.load("spr_patrone.png")

    def fire(self):
        self.is_fired = True

    def update(self):
        self.y -= self.bullet_speed  # Geschoss nach oben bewegen
        if self.y <= 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.x, self.y))

    def check_collision(self, enemy):
        #Kollisionerkennung: Prüfen, ob sich die Rechtecke von Schuss und Alien überlappen
        bullet_rect = self.bullet_img.get_rect(topleft=(self.x,self.y))

