import random
import pygame
print(pygame.version.ver)

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Танки 2Д")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 26)
player = pygame.Rect(275, 420, 50, 50)
enemy = pygame.Rect(random.randint(0, 550), 0, 50, 50)
bullets = []
score = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(player.centerx - 3, player.top, 6, 14))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    player.clamp_ip(screen.get_rect())
    enemy.y += 2
    
    for bullet in bullets[:]:
        bullet.y -= 8
        if bullet.colliderect(enemy):
            bullets.remove(bullet)
            score += 1
            enemy.topleft = (random.randint(0, 550), -50)
        elif bullet.bottom < 0:
            bullets.remove(bullet)

    if enemy.top > 500 or enemy.colliderect(player):
        score = 0
        enemy.topleft = (random.randint(0, 550), -50)

pygame.quit()
