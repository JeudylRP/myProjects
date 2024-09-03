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
------- 12. Kollision zwischen Alien und Geschoss erfassen
------- 13. Game Over implementieren
------- 14.Punktestand-Anzeige implementieren 00:00
------- 15.
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
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))
        self.background_img = pygame.image.load("spr_space_himmel.png")

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break

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
                                self.enemies.remove(enemy)  # Entfernt das getroffene Alien
                                self.spaceship.bullets.remove(bullet)  # Entfernt den Schuss
                                break  # Verhindert Probleme bei der Iteration über die Liste
                    else:
                        self.spaceship.bullets.remove(bullet)

            for enemy in self.enemies:
                enemy.update()
                # Überprüfen, ob ein Alien den unteren Rand erreicht hat
                if enemy.y > 460:
                    for i in self.enemies:
                        i.y = 1000  # Verschiebe alle Aliens aus dem Bildschirm, um das Spiel zu beenden
                    self.print_game_over()
                    self.running = False  # Spiel anhalten nach Game Over
                    pygame.display.update()  # Aktualisiere die Anzeige, um "GAME OVER" anzuzeigen
                    pygame.time.wait(2000)  # Warte 2 Sekunden, damit der Spieler die Nachricht sehen kann
                    break

            pygame.display.update()

        pygame.quit()  # Beende Pygame ordnungsgemäß nach dem Spiel

    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))
        self.screen.blit(go_text, (200, 250))


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
        self.bullets[-1].fire()

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
        # Kollisionerkennung: Prüfen, ob sich die Rechtecke von Schuss und Alien überlappen
        bullet_rect = self.bullet_img.get_rect(topleft=(self.x, self.y))
        enemy_rect = enemy.enemy_img.get_rect(topleft=(enemy.x, enemy.y))
        return bullet_rect.colliderect(enemy_rect)


class Enemy:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 5
        self.change_y = 60
        self.game = game
        self.enemy_img = pygame.image.load("spr_space_enemy.png")

    def update(self):
        self.x += self.change_x
        if self.x >= 736:
            self.y += self.change_y
            self.change_x = -5
        elif self.x <= 0:
            self.y += self.change_y
            self.change_x = 5
        self.game.screen.blit(self.enemy_img, (self.x, self.y))


if __name__ == "__main__":
    game = Game(800, 600)
    game.run()  # Startet das Spiel
