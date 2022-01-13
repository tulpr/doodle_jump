from screens.shop_screen import *
from screens.rules_screen import *
from screens.play_screen import *
import os


def end_screen(count_mora):
    while True:
        image = pygame.image.load('data\\screens_foto\\end.jpg')
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
        screen.blit(fon, (0, 0))
        pygame.display.flip()
