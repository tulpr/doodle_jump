from functions import load_image, mora_in_db, mora_from_db, get_slime_name, get_skin_id, get_skins_bool, new_skin, \
    change_skin
from const import *
from terminate import *


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