import pygame as pg

pg.init()

Clock = pg.time.Clock()
Info = pg.display.Info()

current_w, current_h = Info.current_w, Info.current_h
screen = pg.display.set_mode((current_w, current_h - 60))

black = (0, 0, 0)
red = (255, 0, 0)

