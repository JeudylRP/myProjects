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
------- 11. Kollision zwischen Alien und Geschoss erfassen 00:00
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
                    if event.key == pygame.K_SPACE:
                        self.spaceship.fire_bullet()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.spaceship.move(0)

            self.spaceship.update()
            '''
            Erklärung von "self.spaceship.update()":
            - 'self.spaceship:' Das ist dein Raumschiff im Spiel.
            Es ist wie ein Spielzeug, das du steuern kannst.
            - 'update()': Das bedeutet "aktualisieren" oder "erneuern". Jedes Mal,
            wenn das Spiel einen neuen Moment zeigt (wie in einem Film, der Bild für Bild abläuft),
            soll das Raumschiff an der richtign Stelle sein.
            
            Wenn wir self.spaceship.update(), aufrufen, sagt das dem Spiel:
            "Hey, schau nach, wo das Raumschiff, gerade ist, bewege es, wenn es sich bewegen soll,
            und zeichne es dann neu auf dem Bildschirm"
            
            Ds hilft dabei, das Raumschiff in jedem Bild an der richtigen Stelle z zeigen, ob es nun 
            stillsteht oder sich bewegt.
            '''
            if len(self.spaceship.bullets) > 0:
                for bullet in self.spaceship.bullets:
                    if bullet.is_fired:
                        bullet.update()

                    else:
                        self.spaceship.bullets.remove(bullet)

            for enemy in self.enemies:
                enemy.update()

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
        self.bullets[len(self.bullets)-1].fire()


    '''"Erklärung von 'self.bullets[len(self.bullets)-1].fire()"
    - "self.bullets": Das ist eine Liste, also eine rt Sammlung von allen Kugeln (oder Schüssen), die dein Raumschiff abgefeuert hat.
    - "len(self.bullets)": Das zählt, wie viele Kugeln gerade in der Liste sind.
    Wenn du zum Beispiel 3 Kugeln abgefeuert hast, dass wäre 'len(self.bullets)'
    gleich 3
    - "len(self.bullets)-1": Das bedeutet "die letze Kugel in der Liste". Wenn es 3 Kugeln gibt, dass wäre
    'len(self.bullets)-1' gleich 2, weil wir bei 0 anfangen zu zählen (0 ist die erste Kugel, 1 ist die zweite, 2 ist die dritte).
    
    - self.bullets[len(self.bullets)-1]: Das wählt die letze Kugel aus, die du gerade abgefeuert hast.
    - "fire()": Das bedeutet, dass diese Kugel abgeschossen wird
    
    Also, wenn du "self.bullets[len(self.bullets)-1].fire()"
    schreibst, sagst du dem Spiel: "Nimm die letze Kugel, die ich abgefeuert habe, und schiesse sie jetzt wircklich los!"
    
    Es sorgt dafür, dass die neueste Kugel in Bewegung gesetzt wird und auf dem Bildschirm nach oben fliegt 
    '''
    def move(self,speed):
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
        self.y -=self.bullet_speed #Geschoss nach oben bewegen
        if self.y <= 0:
            self.is_fired = False
        self.game.screen.blit(self.bullet_img, (self.x, self.y))

class Enemy:
    def __init__(self, game, x,y):
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
    print(len(game.spaceship.bullets))
























