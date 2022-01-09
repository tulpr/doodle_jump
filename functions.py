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
    cur.execute(f"UPDATE mora SET count = count + {count}")
    con.commit()
    con.close()


def mora_from_db():
    con = sqlite3.connect("jump.db")
    cur = con.cursor()
    mora = cur.execute("SELECT count FROM mora").fetchone()
    con.commit()
    con.close()
    return mora[0]


def get_slime_name():
    con = sqlite3.connect("jump.db")
    cur = con.cursor()
    name = cur.execute("SELECT name FROM skin").fetchone()
    con.commit()
    con.close()
    return name[0]


def get_skin_id():
    con = sqlite3.connect("jump.db")
    cur = con.cursor()
    num = cur.execute("SELECT number FROM skin").fetchone()
    con.commit()
    con.close()
    return num[0]


def get_skins_bool():
    con = sqlite3.connect("jump.db")
    cur = con.cursor()
    list1 = cur.execute("SELECT 'have or not' FROM slimes").fetchall()
    con.commit()
    con.close()
    return list1


pygame.quit()
