import pygame
from load_image import load_image
from Background import Background

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doodle jump')

BackGround = Background('data\\background.png', [0, 0])


# создадим группу, содержащую все спрайты
all_sprites = pygame.sprite.Group()
hero_img = load_image('slime.png')
hero_img = pygame.transform.scale(hero_img, (130, 100))
hero = pygame.sprite.Sprite(all_sprites)
# создадим спрайт
# sprite = pygame.sprite.Sprite()
hero.image = hero_img
hero.rect = hero.image.get_rect()
dist = 10

running = True
jump_flag = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keys = pygame.key.get_pressed()
        # if key[pygame.K_DOWN]:
        #     hero.rect.top += dist
        # if keys[pygame.K_SPACE]:
        #     hero.rect. += dist
        if keys[pygame.K_RIGHT]:
            hero.rect.left += dist
        if keys[pygame.K_LEFT]:
            hero.rect.left -= dist

    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    all_sprites.draw(screen)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
