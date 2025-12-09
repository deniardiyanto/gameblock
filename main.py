import pygame
import random
import sys

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
WIDTH, HEIGHT = 300, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Box")

# Warna
WHITE = (255, 255, 255)
BLUE = (50, 100, 255)
RED = (255, 50, 50)

# Kecepatan frame
clock = pygame.time.Clock()
FPS = 30

# Player
player_size = 50
player = pygame.Rect(WIDTH//2, HEIGHT-60, player_size, player_size)
player_speed = 5

# Box jatuh
box_size = 40
box = pygame.Rect(random.randint(0, WIDTH-box_size), 0, box_size, box_size)
box_speed = 5

score = 0
font = pygame.font.Font(None, 36)

# Loop utama
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Kontrol player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Gerak box
    box.y += box_speed
    if box.y > HEIGHT:
        box.y = 0
        box.x = random.randint(0, WIDTH - box_size)

    # Cek tumbukan
    if player.colliderect(box):
        score += 1
        box.y = 0
        box.x = random.randint(0, WIDTH - box_size)

    # Gambar
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, box)

    # Tampilkan skor
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
