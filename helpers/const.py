import pygame

pygame.font.init()
pygame.init()
pygame.mixer.music.load('data\\music\\Genshin music.mp3')
pygame.mixer.music.play()
size = WIDTH, HEIGHT = 500, 600
myfont = pygame.font.SysFont('Comic Sans MS', 20)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Doodle jump')
