
import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 400))
player = pygame.Rect(50, 50, 20, 20)

# Generate 10 random obstacles
obstacles = [pygame.Rect(random.randint(0, 380), random.randint(0, 380), 20, 20) for _ in range(10)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 2
    if keys[pygame.K_RIGHT]:
        player.x += 2

    screen.fill(0)
    pygame.draw.rect(screen, (0, 0, 255), player)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
