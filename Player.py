import pygame

from Background import Background
from load_image import load_image

pygame.init()

clock = pygame.time.Clock()
FPS = 60

size = [800, 600]
tile_size = 50
game_over = False
score = 0
display = pygame.display.set_mode(size)
background = Background('data\\background.png', [0, 0])
# background = pygame.transform.scale(background, size)
all_sprites = pygame.sprite.Group()
hero_img = load_image('slime.png')
hero_img = pygame.transform.scale(hero_img, (130, 100))
hero = pygame.sprite.Sprite(all_sprites)


class Player():
    def __init__(self, left, bottom):
        self.images_right = []
        self.images_left = []
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_left.append(img_left)
            self.images_right.append(img_right)
        # self.dead_img = pygame.image.load('img/ghost.png')
        self.index = 0
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.bottom = bottom
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.jump = False
        self.direction = 0
        self.score = 0
        self.vel_y = 0
        self.counter = 0

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5
        global game_over
        if not game_over:
            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE] and not self.jump and self.vel_y == 0:
                self.vel_y = -17
                self.jump = True
            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1
            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1
            if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            if self.counter > walk_cooldown:
                self.counter = 0
                self.index = (self.index + 1) % len(self.images_right)
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]

            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10

            dy += self.vel_y

            self.rect.x += dx
            self.rect.y += dy

            if pygame.sprite.spritecollide(self, False) or pygame.sprite.spritecollide(self,
                                                                                       False):
                game_over = True

        if game_over:
            self.image = self.dead_img
            if self.rect.y > 200:
                self.rect.y -= 5

        display.blit(self.image, self.rect)


# class World():
#     def __init__(self, world_map):
#         self.tile_list = []
#
#         grass_img = pygame.image.load('img/grass.png')
#
#         row_count = 0
#         for row in world_map:
#             col_count = 0
#             for tile in row:
#                 if tile == 'P':
#                     global player
#                     player = Player(col_count * tile_size, (row_count + 1) * tile_size)
#
#                 col_count += 1
#             row_count += 1
#         print(self.tile_list)
#
#     def draw(self):
#         for tile in self.tile_list:
#             display.blit(tile[0], tile[1])


# world = World(world_map)
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # display.blit(background, (0, 0))
    # world.draw()
    hero.update()
    display.blit(background.image, background.rect)
    all_sprites.draw(display)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
