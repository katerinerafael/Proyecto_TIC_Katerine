import pygame
import random
import sys
import time

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter 2D - Top Down")
clock = pygame.time.Clock()

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Jugador
player = pygame.Rect(WIDTH // 2, HEIGHT - 60, 50, 50)
player_speed = 5

# Balas
bullets = []
bullet_speed = -7

# Enemigos
enemies = []
enemy_speed = 2
spawn_timer = 0

# Fuente para FPS
font = pygame.font.SysFont(None, 30)

# Temporizador de 10 segundos
start_time = time.time()
run_duration = 10  # Duración en segundos

# Main loop
while True:
    dt = clock.tick(60)
    fps = clock.get_fps()
    screen.fill((0, 0, 0))

    # Salir después de 10 segundos
    if time.time() - start_time >= run_duration:
        break

    # --- Eventos ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # --- Movimiento del jugador ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x += player_speed
    if keys[pygame.K_SPACE]:
        if len(bullets) < 10:  # Limite de balas
            bullets.append(pygame.Rect(player.centerx - 5, player.y, 10, 20))

    # --- Actualizar balas ---
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # --- Generar enemigos ---
    spawn_timer += dt
    if spawn_timer > 500:
        spawn_timer = 0
        enemies.append(pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40))

    # --- Actualizar enemigos ---
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # --- Colisiones ---
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # --- Dibujar ---
    pygame.draw.rect(screen, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # --- Mostrar FPS ---
    fps_text = font.render(f"FPS: {int(fps)}", True, WHITE)
    screen.blit(fps_text, (10, 10))

    pygame.display.flip()

# Al final, antes de salir (antes de sys.exit())
average_fps = clock.get_fps()
with open("fps_log.txt", "w") as f:
    f.write(f"{average_fps}\n")

# Guardar resultados del benchmark
with open("resultados/vm_fps.csv", "a") as f:
    f.write(f"{fps:.2f}\n")

# Salir del juego
pygame.quit()
sys.exit()
