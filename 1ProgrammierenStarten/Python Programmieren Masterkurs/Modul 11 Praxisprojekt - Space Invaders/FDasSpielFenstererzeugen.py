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
------- 14.Punktestand-Anzeige implementieren WIEDERHOLEN
'''

import pygame  # Importiert die Pygame-Bibliothek, die für die Grafik- und Spieleentwicklung verwendet wird
import random  # Importiert die Random-Bibliothek, um Zufallszahlen zu erzeugen
import math  # Importiert die Math-Bibliothek, um mathematische Funktionen zu nutzen


# Die Game-Klasse steuert das gesamte Spiel
class Game:
    def __init__(self, width, height):
        pygame.init()  # Initialisiert alle Pygame-Module
        self.width = width  # Legt die Breite des Spielfensters fest
        self.height = height  # Legt die Höhe des Spielfensters fest
        self.screen = pygame.display.set_mode(
            (self.width, self.height))  # Erstellt ein Spielfenster mit der angegebenen Breite und Höhe
        pygame.display.set_caption("Space Invaders")  # Setzt den Titel des Fensters auf 'Space Invaders'
        self.clock = pygame.time.Clock()  # Erstellt eine Uhr, um die Bildwiederholrate zu steuern (Klammern hinzugefügt)
        self.running = True  # Gibt an, ob das Spiel läuft
        self.spaceship = Spaceship(self, 370, 515)  # Erstellt ein Raumschiff an den Koordinaten (370, 515)
        self.score = 0  # Initialisiert den Punktestand auf 0
        self.enemies = []  # Erstellt eine Liste, um die Aliens zu speichern

        # Erstellt 12 Aliens an zufälligen Positionen und fügt sie der Liste hinzu
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))

        self.background_img = pygame.image.load("spr_space_himmel.png")  # Lädt das Hintergrund für das Spiel

    def run(self):  # Füge eine 'run'-Methode hinzu, um die Hauptschleife zu starten
        # Hauptspiel-Schleife, die das Spiel im Laufen hält
        while self.running:
            self.clock.tick(60)  # Stellt das Spiel auf 60 Frames pro Sekunde ein
            self.screen.blit(self.background_img, (0, 0))  # Zeichnet den Hintergrund auf dem Bildschirm

            # Überprüft alle Ereignisse wie Tastatureingaben oder das Schließen des Fensters
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Wenn das Fenster geschlossen wird
                    self.running = False  # Beendet die Spielschleife

                if event.type == pygame.KEYDOWN:  # Wenn eine Taste gedrückt wird
                    if event.key == pygame.K_LEFT:  # Links-Pfeiltaste
                        self.spaceship.move(-10)  # Bewegt das Raumschiff nach links
                    if event.key == pygame.K_RIGHT:  # Rechts-Pfeiltaste
                        self.spaceship.move(10)  # Bewegt das Raumschiff nach rechts
                    if event.key == pygame.K_SPACE:  # Leertaste
                        self.spaceship.fire_bullet()  # Feuert eine Kugel ab
                if event.type == pygame.KEYUP:  # Wenn eine Taste losgelassen wird
                    if event.key == pygame.K_LEFT:  # Links-Pfeiltaste losgelassen
                        self.spaceship.move(0)  # Hört auf, sich nach links zu bewegen
                    if event.key == pygame.K_RIGHT:  # Rechts-Pfeiltaste losgelassen
                        self.spaceship.move(0)  # Hört auf, sich nach rechts zu bewegen

            self.spaceship.update()  # Aktualisiert die Position des Raumschiffs

            # Überprüft, ob es Kugeln gibt, die aktualisiert werden müssen
            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:  # Wenn die Kugel abgefeuert wurde
                        bullet.update()  # Aktualisiert die Position der Kugel
                    else:
                        self.spaceship.bullets.remove(bullet)  # Entfernt die Kugel, wenn sie nicht mehr aktiv ist

            # Aktualisiert die Position und den Zustand der Aliens
            for enemy in self.enemies:
                enemy.update()
                enemy.check_collision()  # Überprüft, ob eine Kugel ein Alien getroffen hat
                if enemy.y > 460:  # Wenn ein Alien den unteren Rand des Bildschirms erreicht
                    for i in self.enemies:
                        i.y = 1000  # Verschiebt alle Aliens aus dem Bild (Game Over)
                    self.print_game_over()  # Zeigt das "Game Over"-Zeichen an
                    break  # Beendet die Spielschleife

            self.print_score()  # Zeigt den Punktestand an
            pygame.display.update()  # Aktualisiert den Bildschirm

    # Funktion zum Anzeigen des "Game Over"-Textes
    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)  # Legt die Schriftart und -größe für den Text fest
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))  # Erstellt den Text "GAME OVER" in Weiß
        self.screen.blit(go_text, (200, 250))  # Zeichnet den Text in der Mitte des Bildschirms

    # Funktion zum Anzeigen des Punktestands
    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 24)  # Legt die Schrift und -größe für den Punktestand fest
        score_text = score_font.render("Punkte: " + str(self.score), True, (255, 255, 255))  # Erstellt den Punktestand
        self.screen.blit(score_text, (8, 8))  # Zeichnet den Punktestand oben links auf den Bildschirm


# Klasse, die das Raumschiff steuert
class Spaceship:
    def __init__(self, game, x, y):
        self.x = x  # X-Position des Raumschiffs
        self.y = y  # Y-Position des Raumschiffs
        self.change_x = 0  # Geschwindigkeit des Raumschiffs
        self.game = game  # Referenz auf das Game-Objekt
        self.spaceship_img = pygame.image.load("spr_spaceship.png")  # Lädt das Bild des Raumschiffs
        self.bullets = []  # Liste, um die Kugeln zu speichern (korrekt initialisiert)

    # Funktion zum Abfeuern einer Kugel
    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))  # Fügt eine neue Kugel zur Liste hinzu
        self.bullets[-1].fire()  # Feuert die zuletzt hinzugefügte Kugel ab

    # Funktion, um die Bewegungsgeschwindigkeit des Raumschiffs zu ändern
    def move(self, speed):
        self.change_x = speed  # Ändert die Geschwindigkeit des Raumschiffs

    # Funktion, um die Position des Raumschiffs zu aktualisieren
    def update(self):
        self.x += self.change_x  # Bewegt das Raumschiff nach links oder rechts
        if self.x < 0:  # Begrenzung, damit das Raumschiff nicht aus dem Bildschirm nach links verschwindet
            self.x = 0
        elif self.x > 736:  # Begrenzung, damit das Raumschiff nicht aus dem Bildschirm nach rechts verschwindet
            self.x = 736
        self.game.screen.blit(self.spaceship_img, (self.x, self.y))  # Zeichnet das Raumschiff auf den Bildschirm


# Klasse, die die Kugeln (Schüsse) steuert
class Bullet:
    def __init__(self, game, x, y):
        self.x = x  # X-Position der Kugel
        self.y = y  # Y-Position der Kugel
        self.game = game  # Referenz auf das Game-Objekt
        self.is_fired = False  # Gibt an, ob die Kugel abgefeuert wurde
        self.bullet_speed = 10  # Geschwindigkeit der Kugel
        self.bullet_img = pygame.image.load("spr_patrone.png")  # Lädt das Bild der Kugel

    # Funktion, um die Kugel abzufeuern
    def fire(self):
        self.is_fired = True  # Setzt den Status der Kugel auf "abgefeuert"

    # Funktion, um die Position der Kugel zu aktualisieren
    def update(self):
        self.y -= self.bullet_speed  # Bewegt die Kugel nach oben
        if self.y <= 0:  # Wenn die Kugel den oberen Rand des Bildschirms erreicht
            self.is_fired = False  # Setzt den Status der Kugel auf "nicht abgefeuert"
        self.game.screen.blit(self.bullet_img, (self.x, self.y))  # Zeichnet die Kugel auf den Bildschirm


# Klasse, die die Aliens steuert
class Enemy:
    def __init__(self, game, x, y):
        self.x = x  # X-Position des Aliens
        self.y = y  # Y-Position des Aliens
        self.change_x = 5  # Geschwindigkeit der horizontalen Bewegung
        self.change_y = 60  # Geschwindigkeit der vertikalen Bewegung
        self.game = game  # Referenz auf das Game-Objekt
        self.enemy_img = pygame.image.load("spr_space_enemy.png")  # Lädt das Bild des Aliens

    def check_collision(self):
        for bullet in self.game.spaceship.bullets:
            # Berechnet die Distanz zwischen dem Alien (self) und der Kugel (bullet) mit dem Satz des Pythagoras
            distance = math.sqrt(math.pow(self.x - bullet.x, 2) + math.pow(self.y - bullet.y, 2))

            # Wenn die Distanz kleiner als 35 Pixel ist, wird eine Kollision festgestellt
            if distance < 35:
                bullet.is_fired = False  # Setzt die Kugel auf "nicht abgefeuert"
                self.game.score += 1  # Erhöht den Punktestand des Spiels um 1
                # Setzt die Position des Aliens zufällig neu
                self.x = random.randint(0, 736)  # Neue X-Position des Aliens
                self.y = random.randint(50, 150)  # Neue Y-Position des Aliens

    def update(self):
        self.x += self.change_x  # Bewegt das Alien horizontal (links oder rechts)
        if self.x >= 736:  # Wenn das Alien den rechten Rand des Spielfelds erreicht
            self.y += self.change_y  # Bewegt das Alien nach unten
            self.change_x = -5  # Ändert die Richtung der Bewegung nach links
        elif self.x <= 0:  # Wenn das Alien den linken Rand des Spielfelds erreicht
            self.y += self.change_y  # Bewegt das Alien nach unten
            self.change_x = 5  # Ändert die Richtung der Bewegung nach rechts
        self.game.screen.blit(self.enemy_img, (self.x, self.y))  # Zeichnet das Alien auf den Bildschirm


if __name__ == "__main__":
    game = Game(800, 600)  # Erstellt ein neues Spiel mit einer Fenstergröße von 800x600
    game.run()  # Startet das Spiel
