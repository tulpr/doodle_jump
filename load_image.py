import os
import sys
import pygame
import sqlite3

pygame.init()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((250, 250))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def mora_in_db(count):
    con = sqlite3.connect("jump.db")
    cur = con.cursor()
    cur.execute(f"UPDATE records SET last = {count}")
    cur.execute(f"UPDATE records SET max = {count} WHERE max < {count}")
    con.commit()
    con.close()


pygame.quit()
