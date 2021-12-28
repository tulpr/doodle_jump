import pygame
import sys
from load_image import load_image
from Background import Background
from math import cos, pi

pygame.init()
size = WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doodle jump')


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    image = pygame.image.load('data\\start.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    rules_screen()
                elif event.key == pygame.K_x:
                    terminate()
                elif event.key == pygame.K_m:
                    shop_screen()
                elif event.key == pygame.K_a:
                    play_screen()
        pygame.display.flip()


def rules_screen():
    image = pygame.image.load('data\\rules.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start_screen()
        pygame.display.flip()


def shop_screen():
    image = pygame.image.load('data\\shop.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    start_screen()
        pygame.display.flip()


def play_screen():
    image = pygame.image.load('data\\play.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))

    # создадим группу, содержащую все спрайты
    all_sprites = pygame.sprite.Group()
    hero_img = load_image('slime.png')
    hero_img = pygame.transform.scale(hero_img, (130, 100))
    hero = pygame.sprite.Sprite(all_sprites)
    # создадим спрайт
    # sprite = pygame.sprite.Sprite()
    hero.image = hero_img
    hero.rect = hero.image.get_rect().move((WIDTH - 130) // 2, (HEIGHT - 100) * 0.8)
    dist = 10

    running = True
    jump_flag = False
    time = 0
    freq = 0.001
    mag = 50
    while running:
        time += 1
        h_t = 350
        hero.rect.top = h_t + mag * cos(2*pi*freq*time)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keys = pygame.key.get_pressed()
            # if key[pygame.K_DOWN]:
            #     hero.rect.top += dist
            if keys[pygame.K_SPACE]:
                pass
            if keys[pygame.K_RIGHT]:
                hero.rect.left += dist
            if keys[pygame.K_LEFT]:
                hero.rect.left -= dist
        screen.blit(fon, (0, 0))
        all_sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()


start_screen()
