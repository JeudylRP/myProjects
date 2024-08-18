'''
------- 5. Das Spielfenster erzeugen.
------- 6. Titel, Framerate und Hintergrund modifizieren.
------- 7. Das Raumschiff platzieren.
------- 8. Bewegungsmechaniken implementieren.
------- 9. Bewegung eingrenzen.
------- 10. Geschoss implementieren 00:00
'''

import pygame


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
        self.background_img = pygame.image.load("spr_space_himmel.png")

        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0, 0))
            '''
            1. self.screen: Dies ist die Oberfläche, auf der alle
            Grafiken des Spiels gezeichnet werden.
            Sie repräsentiert das Spielfenster.
            
            2. blit(): Dies ist eine Methode in Pygame, die
            verwendet wird, um eine Oberfläche (z.B. ein Bild)
            auf eine andere Oberfläche zu kopieren.
            Mit anderen Worten, sie "malt" das Bild auf das Spielfenster.
            
            3. self.background_img: Dies ist das Bild, das als Hintergrund
            verwendet wird. Es wird auf die Oberfläche ('self.screen') gezeichnet.
            
            4. '(0,0)': Dies gibt die Position an, an der das Bild auf dem
            Bildschirm gezeichnet werden soll. '(0,0)'
            bedeutet die linke obere Ecke des Spielfensters.            
            '''

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move(-10)
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move(10)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.spaceship.move(0)

            self.spaceship.update()
            pygame.display.update()


class Spaceship:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.game = game
        self.spaceship_img = pygame.image.load("spr_spaceship.png")

    def move(self, speed):
        self.change_x = speed

        '''
        Die Funktion 'move(self, speed)' legt fest, wie schnell sich
        das Raumschiff horizontal bewegen soll. Wenn du eine Taste
        drückst (z.B. die linke oder rechte Pfeiltaste), wird der Wert
        'speed' an die Funktion übergeben, und die Variable 'self.change_x'
        wird entsprechend angepasst. Dieser Wert wird später in der Funktion
        'update' verwendet, um das Raumschiff zu verschieben.
        '''

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        elif self.x > 736:
            self.x = 736
        '''
        Die Zahl 736 kommt daher, dass dein Spielfenster eine Breite von 800 Pixeln hat.
        Wenn das Raumschiff 64 Pixel breit ist (das ist eine typische Breite für Spiel-Sprites),
        musst du sicherstellen, dass es nicht über den rechten Rand des Bildschirms hinausgeht.
        
        Das Bedeutet:
        1. Die Breite des Spielfensters beträgt 800 Pixel.
        2. Wenn das Raumschiff gaanz rechts auf dem Bildschirm 
        sein soll, sollte, sollte seine x-Position so sein, dass der
        rechte Rand des Raumschiffs 800 Pixel beträgt.
        
        Da das Raumschiff 64 Pixel breit ist:
        - Di Maximale x-Position, bei der das Raumschiff noch komplett auf
        dem Bildschirm ist, wäre 800-64 = 736 Pixel
        Deshalb setzt du die grenze bei 736, damit das Raumschiff nicht über
        den rechten Bildschirmrad hinaus rutscht.         
        '''

        self.game.screen.blit(self.spaceship_img, (self.x, self.y))

if __name__ == "__main__":
    game=Game(800,600)


