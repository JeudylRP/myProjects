'''
------- 5. Das Spielfenster erzeugen:
------- 6. Titel, Framerate und Hintergrund modifizieren
'''
import pygame 

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((set.width, self.height))
        pygame.display.set_caption("Space Invaders")
        self.clock = pygame.time.Clock()
        self.running = True

        self.background_img = pygame.image.load("spr_space_background.png")

        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()



if __name__ == "__main__":
     game = Game(800,600)










