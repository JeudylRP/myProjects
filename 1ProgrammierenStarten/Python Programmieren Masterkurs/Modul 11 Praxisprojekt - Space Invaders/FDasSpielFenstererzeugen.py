'''
------- 5. Das Spielfenster erzeugen:
------- 6. Titel, Framerate und Hintergrund modifizieren
------- 7. Das Raumschiff platzieren
'''
import pygame

class Game:
    def __init__(self,width,height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True
        self.spaceship = Spaceship(self,370,515)

        self.background_img = pygame.image.load("spr_space_himmel.png")

        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.spaceship.draw()
            pygame.display.update()

class Spaceship:
 def __init__(self,game,x,y):
    self.x = x
    self.y = y
    self.game = game
    self.spaceship_img=pygame.image.load("spr_spaceship.png")


 def draw(self):
     self.game.screen.blit(self.spaceship_img, (self.x,self.y))


if __name__=="__main__":
    game = Game(800,600)


