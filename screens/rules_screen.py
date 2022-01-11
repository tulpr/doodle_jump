from helpers.const import *
from helpers.terminate import *


def rules_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return
        image = pygame.image.load('data\\screens_foto\\rules.jpg')
        fon = pygame.transform.scale(image, (WIDTH, HEIGHT))
        screen.blit(fon, (0, 0))
        pygame.display.flip()
