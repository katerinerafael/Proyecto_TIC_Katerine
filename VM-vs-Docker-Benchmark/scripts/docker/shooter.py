import os
os.environ["SDL_VIDEODRIVER"] = "dummy"  # Desactiva la GUI
os.environ["SDL_AUDIODRIVER"] = "dummy"  # <--- evita error ALSA

import pygame
import random
import sys
import time

# Inicializar Pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter 2D - Benchmark")
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

# Simulación automática por 10 segundos
start_time = time.time()
while time.time() - start_time < 10:
    dt = clock.tick(60)
    screen.fill((0, 0, 0))

    # Movimiento automático del jugador (va de lado a lado)
    player.x += player_speed
    if player.x <= 0 or player.x >= WIDTH - player.width:
        player_speed = -player_speed

    # Disparo automático
    if len(bullets) < 10:
        bullets.append(pygame.Rect(player.centerx - 5, player.y, 10, 20))

    # Actualizar balas
    for bullet in bullets[:]:
        bullet.y += bullet_speed
        if bullet.y < 0:
            bullets.remove(bullet)

    # Generar enemigos
    spawn_timer += dt
    if spawn_timer > 500:
        spawn_timer = 0
        enemies.append(pygame.Rect(random.randint(0, WIDTH-40), -40, 40, 40))

    # Actualizar enemigos
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.y > HEIGHT:
            enemies.remove(enemy)

    # Colisiones
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                break

    # Dibujar (aunque no se muestre)
    pygame.draw.rect(screen, WHITE, player)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    pygame.display.flip()

# Guardar promedio de FPS
average_fps = clock.get_fps()
os.makedirs("datos", exist_ok=True)
with open("datos/fps.csv", "a") as f:
    f.write(f"1,{average_fps:.2f}\n")
