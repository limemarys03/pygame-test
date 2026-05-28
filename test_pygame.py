import pygame
import sys

pygame.init()

# Настраиваем размеры экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

hero_x = 336
hero_y = 236
hero_speed = 7

try:
    hero_image = pygame.image.load("hero.png").convert_alpha()
    hero_image = pygame.transform.scale(hero_image, (128, 128))
    has_sprite = True
except:
    has_sprite = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- ТАЧ-УПРАВЛЕНИЕ ДЛЯ ТЕЛЕФОНА ---
    # Проверяем, нажал ли палец на экран в данный момент
    if pygame.mouse.get_pressed()[0]: 
        # Получаем координаты нажатия пальца (X, Y)
        touch_x, touch_y = pygame.mouse.get_pos()
        
        # Логика деления экрана на зоны движения
        if touch_x < WIDTH // 3:        # Кликнули в левую треть экрана
            hero_x -= hero_speed
        elif touch_x > (WIDTH // 3) * 2: # Кликнули в правую треть экрана
            hero_x += hero_speed
            
        if touch_y < HEIGHT // 3:       # Кликнули в верхнюю треть
            hero_y -= hero_speed
        elif touch_y > (HEIGHT // 3) * 2: # Кликнули в нижнюю треть
            hero_y += hero_speed

    screen.fill((20, 20, 35))

    if has_sprite:
        screen.blit(hero_image, (hero_x, hero_y))
    else:
        pygame.draw.rect(screen, (255, 50, 50), (hero_x, hero_y, 128, 128))

    pygame.display.update()
    pygame.display.flip()

pygame.quit()
sys.exit()

