import sys
import pygame as pg
from random import randint

def check_bound(obj_rct,scr_rct):
    if obj_rct.left< scr_rct.left or scr_rct.right < obj_rct.right: hoge
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: fuga

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))

    bg_sfc = pg.image.load("ex04/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    clock = pg.time.Clock()

    tori_sfc = pg.image.load("ex04/8.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct=bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0,1600),randint(0,900)

    vx = +1
    vy=+1

    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:tori_rct.centery -=1
        if key_states[pg.K_DOWN]:tori_rct.centery +=1
        if key_states[pg.K_LEFT]:tori_rct.centerx -=1
        if key_states[pg.K_RIGHT]:tori_rct.centerx +=1
        yoko,tate = check_bomb(tori_rct,scr_rct)
        if yoko == -1 :
            if key_states[pg.K_LEFT]:
                tori_rct.centerx +=1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -=1
        if tate == -1:
            if key_states[pg.K_UP]:tori_rct.centery +=1
            if key_states[pg.K_DOWN]:tori_rct.centery -=1
        scrn_sfc.blit(tori_sfc,tori_rct)
        vx*=yoko
        vy*=tate
        yoko,tate = check_bomb(tori_rct,scr_rct)

        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        
        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()