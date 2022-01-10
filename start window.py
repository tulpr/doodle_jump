import random
import sys

import pygame

from functions import load_image, mora_in_db, mora_from_db, get_slime_name, get_skin_id, get_skins_bool, new_skin, \
    change_skin

pygame.font.init()
pygame.init()
pygame.mixer.music.load('data\\Genshin music.mp3')
pygame.mixer.music.play()
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
        count_mora = mora_from_db()
        mora_count = myfont.render(f'{count_mora}', False, (254, 246, 238))
        image = pygame.image.load('data\\start.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        screen.blit(mora_count, (200, 23))
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
        image = pygame.image.load('data\\shop.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        count_mora = mora_from_db()
        mora_count = myfont.render(f'{count_mora}', False, (254, 246, 238))
        btns = pygame.sprite.Group()
        skins = get_skins_bool()
        skin_id = get_skin_id()
        for i in range(1, 1 + len(skins)):
            if i == skin_id:
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image(f"skin_on.png")
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = 340
                sprite.rect.y = 66 + (93 * (i - 1))
                btns.add(sprite)
            elif skins[i - 1][0] == 'False':
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image(f"{i}not.png")
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = 340
                sprite.rect.y = 66 + (93 * (i - 1))
                btns.add(sprite)
            else:
                sprite = pygame.sprite.Sprite()
                sprite.image = load_image(f"{i}have.png")
                sprite.rect = sprite.image.get_rect()
                sprite.rect.x = 340
                sprite.rect.y = 66 + (93 * (i - 1))
                btns.add(sprite)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
                if event.key == pygame.K_1:
                    if skin_id == 1:
                        break
                    elif skins[0][0] == 'False':
                        mora_in_db(-200)
                        new_skin(1)
                    else:
                        change_skin(1)
                if event.key == pygame.K_2:
                    if skin_id == 2:
                        break
                    elif skins[1][0] == 'False':
                        mora_in_db(-200)
                        new_skin(2)
                    else:
                        change_skin(2)
                if event.key == pygame.K_3:
                    if skin_id == 3:
                        break
                    elif skins[2][0] == 'False':
                        mora_in_db(-200)
                        new_skin(3)
                    else:
                        change_skin(3)
                if event.key == pygame.K_4:
                    if skin_id == 4:
                        break
                    elif skins[3][0] == 'False':
                        mora_in_db(-200)
                        new_skin(4)
                    else:
                        change_skin(4)
                if event.key == pygame.K_5:
                    if skin_id == 5:
                        break
                    elif skins[4][0] == 'False':
                        mora_in_db(-200)
                        new_skin(5)
                    else:
                        change_skin(5)
                if event.key == pygame.K_6:
                    if skin_id == 6:
                        break
                    elif skins[5][0] == 'False':
                        mora_in_db(-1000)
                        new_skin(6)
                    else:
                        change_skin(6)
        screen.blit(fon, (0, 0))
        screen.blit(mora_count, (57, 23))
        btns.draw(screen)
        pygame.display.flip()


def play_screen():
    def draw_hero(x, y, screen, name='slime'):
        # # создадим группу, содержащую все спрайты
        all_sprites = pygame.sprite.Group()
        hero_img = load_image(name + '.png')
        if name == 'slime':
            hero_img = pygame.transform.scale(hero_img, (70, 60))
        if name == 'slime_dendro':
            hero_img = pygame.transform.scale(hero_img, (90, 80))
        if name == 'slime_electro':
            hero_img = pygame.transform.scale(hero_img, (80, 80))
        if name == 'slime_geo':
            hero_img = pygame.transform.scale(hero_img, (80, 70))
        if name == 'slime_pyro':
            hero_img = pygame.transform.scale(hero_img, (70, 60))
        if name == 'paimon':
            hero_img = pygame.transform.scale(hero_img, (70, 120))
        if name == 'mora':
            hero_img = pygame.transform.scale(hero_img, (30, 30))
        if name == 'monster':
            hero_img = pygame.transform.scale(hero_img, (100, 100))
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
    a = 490
    y0 = 0
    v0 = 400
    x = 0
    v = v0
    n_plat = 3
    y_pr = y0
    platforms = [[0, 130], [-100, -50]]
    moras = [0, 0]
    monsters = [0, 0]
    pause = 0
    mus_pause = 0
    volume = 0.5
    fl = 0
    while 1:
        fl -= 1
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
                elif i.key == pygame.K_SPACE:
                    if mus_pause:
                        mus_pause = 0
                    else:
                        mus_pause = 1
                    # pygame.mixer.music.stop()
                elif i.key == pygame.K_o:
                    pygame.mixer.music.unpause()
                    # pygame.mixer.music.play()
                    volume += 0.1
                elif i.key == pygame.K_j:
                    pygame.mixer.music.unpause()
                    volume -= 0.1
                    # pygame.mixer.music.play()
        pygame.mixer.music.set_volume(volume)
        # print(pygame.mixer.music.get_volume())
        # print(volume)
        pygame.time.delay(20)
        if mus_pause:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        if pause == 0:
            col = []
            t += 1 / FPS
            # сгенерируем список платформ длины n_plat
            if len(platforms) <= n_plat:
                platforms.append([random.randrange(-WIDTH // 2, WIDTH // 2, 40),
                                  random.randrange(-int(1.1 * HEIGHT) // 2, -HEIGHT // 2, 60)])
                moras.append(random.randint(0, 1))
                monsters.append(0) if moras[-1] == 1 else monsters.append(random.randint(1, 1))
            y = y0 - v * t + (a * (t ** 2)) / 2
            cc = (y - y_pr) * FPS
            y_pr = y
            screen.blit(fon, (0, 0))
            # pygame.draw.circle(screen, BLUE, (x, y), r)
            hero = draw_hero(x, y, screen, get_slime_name())
            for indx, pl in enumerate(platforms):
                mora_col = 0
                monster_col = 0
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
                if monsters[indx]:
                    monster = draw_hero(pl[0] + 60, pl[1] - 40, screen, name='monster')
                    monster_col = pygame.sprite.collide_rect(hero, monster)

                if monster_col and fl <= 0:
                    if count_mora - 40 > 0:
                        count_mora -= 40
                    else:
                        count_mora = 0
                    fl = 100
        # отрисовка текста
        textsurface = myfont.render(f'Мора: {count_mora}', False, (254, 246, 238))
        # сдвигаем платформы вниз
        for indx, _ in enumerate(platforms):
            platforms[indx][1] += 1
        # удаление платформ вышедшие за край экрана
        for indx, _ in enumerate(platforms):
            if platforms[indx][1] > 100:
                del platforms[indx]
                del moras[indx]
                del monsters[indx]
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
