import pygame
import sys


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
    pass


start_screen()
