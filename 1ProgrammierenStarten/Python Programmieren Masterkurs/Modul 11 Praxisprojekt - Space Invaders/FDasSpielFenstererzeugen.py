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


# Die Game-Kasse steuert das gesamte Spiel
class Game:
    def __init__(self, width, height):
        pygame.init()  # Initialisert alle Pygame-Module
        self.width = width  # Legt die Breite des Spielfensters fest
        self.height = height  # Legt die Höhe des Spielfensters fest
        self.screen = pygame.display.set_mode(
            (self.width, self.height))  # Erstellt ein Spielfenster mit der angegebenen Breite  und Höhe
        pygame.display.set_caption("Space Invaders")  # Setzt den Titel des Fensters auf 'Space Invaders'
        self.clock = pygame.time.Clock  # Erstellt eine Uhr, um die Bildwiederholrate zu steuern
        self.running = True  # Gibt an, ob das Spiel läuft
        self.spaceship = Spaceship(self, 370, 515)  # Erstellt ein Raumschiff an den Koordinaten (370,515)
        self.score = 0  # Initialisiert den Punktbestand auf 0
        self.enemies = []  # Erstellt eine Liste, um die Aliens zu speichern

        # Erstellt 12 Aliens an zufälligen Positionen und fügt sie der Liste hinzu
        for i in range(12):
            self.enemies.append(Enemy(self, random.randint(0, 736), random.randint(30, 130)))

        self.background_img = pygame.image.load("spr_space_himmel.png")  # Lädt das Hintergrund für das Spiel

        # Hauptspiel-Schleife, die das Spiel im laufen hält
        while self.running:
            self.clock.tick(60)  # Stellt das Spiel auf 60 Frames pro Sekunde ein
            self.screen.blit(self.background_img, (0, 0))  # Zeichnet das Hintergrund auf dem Bildschirm

        # Überprüft alle Ereignisse wie Tastureingaben oder das Schliessen des Fensters
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Wenn das Fenster geschlossen wird
                self.running = False  # Beendet die Spelschleife

            if event.type == pygame.KEYDOWN:  # Wenn eine Taste gedrückt wird
                if event.key == pygame.K_LEFT:  # Links-Pfeiltaste
                    self.spaceship.move(-10)  # Bewegt das Raumschiff nach Links
                if event.key == pygame.K_RIGHT:  # Rechts-Pfeiltaste
                    self.spaceship.move(10)  # Bewegt das Raumschiff nach Rechts
                if event.key == pygame.K_SPACE:  # Leertaste
                    self.spaceship.fire_bullet()  # Feurt eine Kugel ab
            if event.type == pygame.KEYUP:  # Wenn eine Taste losgelassen wird
                if event.key == pygame.K_LEFT:  # Links-Pfeiltaste losgelassen
                    self.spaceship.move(10)  # Bewegt das Raumschiff nach Rechts
                if event.key == pygame.K_RIGHT:  # Rechts-Pfeiltaste losgelassen
                    self.spaceship.move(-10)  # Bewegt das Raumschiff nach Links

        self.spaceship.update()  # Aktualisiert die Position des Raumschiffs

        # Überprüft, ob es Kugeln gibt, die aktualisiert werden müssen
        if len(self.spaceship.bullets) > 0:
            for bullet in self.spaceship.bullets:
                if bullet.is_fired:  # Wenn die Kugel abgefeuert wurde
                    bullet.update()  # Aktualisiert die Position der Kugel#
                else:
                    self.spaceship.bullets.remove(bullet)  # Entfernt die Kugel, wenn dei nicht mehr aktiv ist

        # Aktualisiert die Position und den Zustand der Aliens
        for enemy in self.enemies:
            enemy.update()
            enemy.check_collision()  # Überprüft, ob eine Kugel ein Alien getroffen hat
            if enemy.y > 460:  # Wenn ein Alien den unteren Rand des Bildschirms  erreicht
                for i in self.enemies:
                    i.y = 1000  # Verschiebt alle Aliens aus dem Bild (Game Over)
                self.print_game_over()  # Zeigt das "Game Over"-Zeichen an
                break  # Beendet die Speleschleife

        self.print_score()  # Zeigt den Punktestand an
        pygame.display.update()  # Aktualisiert den Bildschirm

    # Funktion zum Anzeigen des Game Over'-Textes
    def print_game_over(self):
        go_font = pygame.font.Font("freesansbold.ttf", 64)  # Legt die Schriftart und -grösse für den Text fest
        go_text = go_font.render("GAME OVER", True, (255, 255, 255))  # Erstellt den Text "GAME OVER" in weiss
        self.screen.blit(go_text, (200, 250))  # Zeichnet den Text in der Mitte des Bildschirms

    # Funktion zum Anzeigen des Punktestands
    def print_score(self):
        score_font = pygame.font.Font("freesansbold.ttf", 24)  # Legt die Schrift und -grösse für den Punktbestand fest

        score_text = score_font.render("Punkte:" + str(self.score), True,
                                       (255, 255, 255))  # Erstellt den Punktbestand weiss
        self.screen.blit(score_text, (8, 8))  # Zeichnet den Punktestand oben links auf den Bildschirm


# Klasse, die das Raumschiff steuert
class Spaceship:
    def __init__(self, game, x, y):
        self.x = x  # X-Position des Raumschiffs
        self.y = y  # Y-Position des Raumschiffs
        self.change_x = 0  # Geschwindigkeit des Raumschiffs
        self.game = game  # Refernez auf das Game-Objekt
        self.spaceship_img = pygame.image.load("spr_space.png")  # Lädt das Bild des Raumschiffs
        self.bullets = 0[]  # Liste, um die Kufel zu speichern

    # Funktion zum Abfeuern einer Kugel
    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))  # Fügt eine neue Kugel zur Liste hinzu
        self.bullets[-1].fire()  # Feuert die zuletzt hinzufügende Kugel ab

    # Fuktion zum Abfeuern einer Kugel
    def fire_bullet(self):
        self.bullets.append(Bullet(self.game, self.x, self.y))  # Fügt eine neue Kugel zur Liste hinzu
        self.bullets[-1].fire()  # Feuert die zuletzt hinzugefügte ab

    # Funktion, um die Bewegungsgeschwidigkeit ddes Raumschiffs zu ändern
    def move(self, speed):
        self.change_x += speed  # Ändern die Grschwindigkeit des Raumschiffs

    # Funktion, um die Bewegungsgeschwindigkeit des Raumschiffs zu ändern
    def move(self, speed):
        self.change_x += speed  # Ändern die Gechwindigkeit des Raumschiffs

    # Funktion, um die Position des Raumschiffs zu aktualisieren
    def update(self):
        self.x += self.change_x  # Bewegt das Raumschiff nach links oder rechts
        if self.x < 0:  # Begrenzung, damit das Raumschiff nicht aus dem Bildschirm nach Links verschwindet
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
        self.bullet_speed = 10  # Geschwwindigkeit der Kugel
        self.bullet_img = pygame.image.load("spr_patrone.png")  # Lädt das Bild der Kugel

    # Funktion, um die Kugel abzufeuer
    def fire(self):
        self.is_fired = True #Setzt den Status der Kugel auf "abgefeuert"
