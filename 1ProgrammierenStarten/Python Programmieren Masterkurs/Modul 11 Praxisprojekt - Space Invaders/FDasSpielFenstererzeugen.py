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
    def__init__(self, width, height):
    pygame.init()
    self.width = width
