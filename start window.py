from screens.shop_screen import *
from screens.rules_screen import *
from screens.play_screen import *
import os

PTH = os.getcwd()


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
        image = pygame.image.load('data\\screens_foto\\start.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        screen.blit(mora_count, (200, 23))
        pygame.display.flip()


start_screen()
