import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuraciones de la ventana del juego
width, height = 600, 400
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pac-Man')

# Definir colores
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Definir posición y tamaño de Pac-Man
pacman_size = 20
pacman_x, pacman_y = width // 2, height // 2
pacman_speed = 5

# Ciclo principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obtener todas las teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento de Pac-Man
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Limitar Pac-Man a los bordes de la ventana
    pacman_x = max(0, min(pacman_x, width - pacman_size))
    pacman_y = max(0, min(pacman_y, height - pacman_size))

    # Dibujar todo en la ventana
    window.fill(BLACK)
    pygame.draw.circle(window, YELLOW, (pacman_x, pacman_y), pacman_size)
    pygame.display.flip()

    # Controlar la velocidad del juego
    pygame.time.Clock().tick(30)
