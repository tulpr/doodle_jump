from screens.play_screen import *
from helpers.const import *
from helpers.terminate import *


def record_screen():
    while True:
        image = pygame.image.load('data\\screens_foto\\record.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        rec_dif = get_records()[0]
        last_rec = myfont.render(f'Предыдущая высота: {round(rec_dif[1] / HEIGHT, 2)}', False, (254, 246, 238))
        last_dif = myfont.render(f'Предыдущая сложность: {rec_dif[3]}', False, (254, 246, 238))
        max_rec = myfont.render(f'Рекордная высота: {round(rec_dif[2] / HEIGHT, 2)}', False, (254, 246, 238))
        max_dif = myfont.render(f'Рекордная сложность: {rec_dif[4]}', False, (254, 246, 238))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
                if event.key == pygame.K_x:
                    terminate()
        screen.blit(fon, (0, 0))
        screen.blit(last_rec, (55, 115))
        screen.blit(last_dif, (55, 145))
        screen.blit(max_rec, (55, 175))
        screen.blit(max_dif, (55, 205))
        pygame.display.flip()
