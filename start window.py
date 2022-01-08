import random
import sys

import pygame

from load_image import load_image

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
    # image = pygame.image.load('data\\play.jpg')
    # fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    # screen.blit(fon, (0, 0))
    def draw_hero(x, y, screen, name='slime'):
        # # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        hero_img = load_image(name + '.png')
        if name == 'slime':
            hero_img = pygame.transform.scale(hero_img, (130, 100))
        if name == 'mora':
            hero_img = pygame.transform.scale(hero_img, (30, 30))
        hero = pygame.sprite.Sprite(all_sprites)
        # создадим спрайт
        # sprite = pygame.sprite.Sprite()
        hero.image = hero_img
        hero.rect = hero.image.get_rect().move(x + (WIDTH - 130) // 2, y + (HEIGHT - 100) * 0.8)
        all_sprites.draw(screen)
        return hero

    # dist = 10
    #
    # running = True
    # jump_flag = False
    # time = 0
    # freq = 0.001
    # mag = 80
    # while running:
    #     time += 1
    #     h_t = 350
    #     hero.rect.top = h_t + mag * cos(2 * pi * freq * time)
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
    #
    #
    #         keys = pygame.key.get_pressed()
    #         # if key[pygame.K_DOWN]:
    #         #     hero.rect.top += dist
    #         if keys[pygame.K_SPACE]:
    #             pass
    #         if keys[pygame.K_RIGHT]:
    #             hero.rect.left += dist
    #         if keys[pygame.K_LEFT]:
    #             hero.rect.left -= dist
    #     screen.blit(fon, (0, 0))
    #     all_sprites.draw(screen)
    #     pygame.display.update()
    #     pygame.display.flip()
    image = pygame.image.load('data\\play.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    FPS = 60
    W = 700  # ширина экрана
    H = 300  # высота экрана
    WHITE = (255, 255, 255)
    BLUE = (0, 70, 225)

    # sc = pygame.display.set_mode((W, H))
    clock = pygame.time.Clock()
    t = 0
    a = 300
    y0 = 0
    v0 = 400
    x = 0
    y = 0
    v = v0
    n_plat = 3
    y_pr = y0
    platforms = [[0, 130], [-100, -50]]
    moras = [0, 0]

    while 1:
        col = []
        t += 1 / FPS
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        # сгенерируем список платформ длины n_plat
        if len(platforms) <= n_plat:
            platforms.append([random.randrange(-WIDTH // 2, WIDTH // 2, 40),
                              random.randrange(-int(1.1 * HEIGHT) // 2, -HEIGHT // 2, 60)])
            moras.append(random.randint(0, 1))
        y = y0 - v * t + (a * t ** 2) / 2
        cc = (y - y_pr) * FPS
        y_pr = y
        screen.blit(fon, (0, 0))
        # pygame.draw.circle(screen, BLUE, (x, y), r)
        hero = draw_hero(x, y, screen)
        for indx, pl in enumerate(platforms):
            platform = draw_hero(pl[0], pl[1], screen, name='platform')
            if moras[indx]:
                mora = draw_hero(pl[0] + 60, pl[1] - 40, screen, name='mora')
            col = pygame.sprite.collide_rect(hero, platform)

            if col:
                y0 = y
                t = 0
                v = v0
        # сдвигаем платформы вниз
        for indx, _ in enumerate(platforms):
            platforms[indx][1] += 1
        # удаление платформ вышедшие за край экрана
        for indx, _ in enumerate(platforms):
            if platforms[indx][1] > 100:
                del platforms[indx]
                del moras[indx]
        if y > 100:
            image = pygame.image.load('data\\end.jpg')
            fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
            screen.blit(fon, (0, 0))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= 3
        elif keys[pygame.K_RIGHT]:
            x += 3

        clock.tick(FPS)


start_screen()
