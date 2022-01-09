import random
import sys

import pygame

from load_image import load_image, mora_in_db

pygame.font.init()
pygame.init()
size = WIDTH, HEIGHT = 500, 600
myfont = pygame.font.SysFont('Comic Sans MS', 30)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doodle jump')


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
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
        image = pygame.image.load('data\\start.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()


def rules_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
        image = pygame.image.load('data\\rules.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()


def shop_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
        image = pygame.image.load('data\\shop.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()


def play_screen():
    def draw_hero(x, y, screen, name='slime'):
        # # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        hero_img = load_image(name + '.png')
        if name == 'slime':
            hero_img = pygame.transform.scale(hero_img, (130, 100))
        if name == 'mora':
            hero_img = pygame.transform.scale(hero_img, (30, 30))
        hero = pygame.sprite.Sprite(all_sprites)

        hero.image = hero_img
        hero.rect = hero.image.get_rect().move(x + (WIDTH - 130) // 2, y + (HEIGHT - 100) * 0.8)
        all_sprites.draw(screen)
        return hero

    image = pygame.image.load('data\\play.jpg')
    fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
    screen.blit(fon, (0, 0))
    FPS = 60

    clock = pygame.time.Clock()
    count_mora = 0
    t = 0
    a = 600
    y0 = 0
    v0 = 400
    x = 0
    v = v0
    n_plat = 3
    y_pr = y0
    platforms = [[0, 130], [-100, -50]]
    moras = [0, 0]
    pause = 0

    while 1:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                mora_in_db(count_mora)
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_p:
                    if pause:
                        pause = 0
                    else:
                        pause = 1
        if pause == 0:
            col = []
            t += 1 / FPS
            # сгенерируем список платформ длины n_plat
            if len(platforms) <= n_plat:
                platforms.append([random.randrange(-WIDTH // 2, WIDTH // 2, 40),
                                  random.randrange(-int(1.1 * HEIGHT) // 2, -HEIGHT // 2, 60)])
                moras.append(random.randint(0, 1))
            y = y0 - v * t + (a * (t ** 2)) / 2
            cc = (y - y_pr) * FPS
            y_pr = y
            screen.blit(fon, (0, 0))
            # pygame.draw.circle(screen, BLUE, (x, y), r)
            hero = draw_hero(x, y, screen)
            for indx, pl in enumerate(platforms):
                mora_col = 0
                platform = draw_hero(pl[0], pl[1], screen, name='platform')
                if moras[indx]:
                    mora = draw_hero(pl[0] + 60, pl[1] - 40, screen, name='mora')
                    mora_col = pygame.sprite.collide_rect(hero, mora)
                col = pygame.sprite.collide_rect(hero, platform)
                if col:
                    y0 = y
                    t = 0
                    v = v0
                if mora_col:
                    count_mora += 10
                    moras[indx] = 0
            # отрисовка текста
            textsurface = myfont.render(f'Мора: {count_mora}', False, (0, 0, 0))
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
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        mora_in_db(count_mora)
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        mora_in_db(count_mora)
                        if event.key == pygame.K_n:
                            return
                        if event.key == pygame.K_x:
                            terminate()
            screen.blit(textsurface, (200, 0))
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                x -= 3
            elif keys[pygame.K_RIGHT]:
                x += 3

            clock.tick(FPS)


start_screen()
