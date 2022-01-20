from screens.shop_screen import *
from screens.rules_screen import *
from screens.play_screen import *
import os


def end_screen(count_mora, record, difficulty):
    while True:
        image = pygame.image.load('data\\screens_foto\\end.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_in_db(count_mora, record, difficulty)
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    end_in_db(count_mora, record, difficulty)
                    return
                if event.key == pygame.K_x:
                    end_in_db(count_mora, record, difficulty)
                    terminate()
        screen.blit(fon, (0, 0))
        pygame.display.flip()
