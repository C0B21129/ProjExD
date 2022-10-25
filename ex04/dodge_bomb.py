import sys
import pygame as pg
from random import randint
import time

def check_bound(obj_rct,scr_rct):
    yoko,tate = +1,+1
    if obj_rct.left< scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1
    return yoko,tate

def check_bound_q(obj_rct,scr_rct):
    yoko,tate = +1,+1
    if obj_rct.left< scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1
    return yoko,tate

def check_bound_z(obj_rct,scr_rct):
    yoko,tate = +1,+1
    if obj_rct.left< scr_rct.left or scr_rct.right < obj_rct.right:
        yoko=-1.15
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate=-1.15
    return yoko,tate

def main():
    pg.display.set_caption("まじで逃げろ！こうかとん")
    scrn_sfc = pg.display.set_mode((1600,900))
    scrn_rct = scrn_sfc.get_rect()

    bg_sfc = pg.image.load("ex04/izakaya.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("ex04/8.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc,0,2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900,400

    tori2_sfc = pg.image.load("ex04/16.png")
    tori2_sfc = pg.transform.rotozoom(tori2_sfc,0,1.0)
    tori2_rct = tori2_sfc.get_rect()
    tori2_rct.center = 900,400

    bomb_sfc = pg.Surface((20,20))
    bomb_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb_sfc,(255,0,0),(10,10),10)
    bomb_rct=bomb_sfc.get_rect()
    bomb_rct.centerx, bomb_rct.centery = randint(0,scrn_rct.width),randint(0,scrn_rct.height)
    vx = +1
    vy=+1

    bomb2_sfc = pg.Surface((40,40))
    bomb2_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb2_sfc,(0,255,0),(10,10),40)
    bomb2_rct=bomb2_sfc.get_rect()
    bomb2_rct.centerx, bomb2_rct.centery = randint(0,scrn_rct.width),randint(0,scrn_rct.height)
    vx2=+1
    vy2=+1

    bomb3_sfc = pg.Surface((20,20))
    bomb3_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb3_sfc,(0,0,255),(10,10),10)
    bomb3_rct=bomb3_sfc.get_rect()
    bomb3_rct.centerx, bomb3_rct.centery = randint(0,scrn_rct.width),randint(0,scrn_rct.height)
    vx3=+1
    vy3=+1

    bomb4_sfc = pg.Surface((20,20))
    bomb4_sfc.set_colorkey((0,0,0))
    pg.draw.circle(bomb4_sfc,(255,255,255),(10,10),10)
    bomb4_rct=bomb4_sfc.get_rect()
    bomb4_rct.centerx, bomb4_rct.centery = randint(0,scrn_rct.width),randint(0,scrn_rct.height)
    vx4=+1
    vy4=+1

    clock = pg.time.Clock()
    font = pg.font.Font(None, 150)
    
    while True:
        scrn_sfc.blit(bg_sfc,bg_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        key_states = pg.key.get_pressed()
        if key_states[pg.K_UP]:tori_rct.centery -=1
        if key_states[pg.K_UP]:tori2_rct.centery -=1
        if key_states[pg.K_DOWN]:tori_rct.centery +=1
        if key_states[pg.K_DOWN]:tori2_rct.centery +=1
        if key_states[pg.K_LEFT]:tori_rct.centerx -=1
        if key_states[pg.K_LEFT]:tori2_rct.centerx -=1
        if key_states[pg.K_RIGHT]:tori_rct.centerx +=1
        if key_states[pg.K_RIGHT]:tori2_rct.centerx +=1
        yoko, tate = check_bound(tori_rct, scrn_rct)
        if yoko == -1 :
            if key_states[pg.K_LEFT]:
                tori_rct.centerx +=1
            if key_states[pg.K_RIGHT]:
                tori_rct.centerx -=1
        if tate == -1:
            if key_states[pg.K_UP]:tori_rct.centery +=1
            if key_states[pg.K_DOWN]:tori_rct.centery -=1
        scrn_sfc.blit(tori_sfc,tori_rct)

        yoko,tate = check_bound(bomb_rct,scrn_rct)
        vx*=yoko
        vy*=tate
        bomb_rct.move_ip(vx,vy)
        scrn_sfc.blit(bomb_sfc,bomb_rct)
        
        yoko,tate = check_bound_q(bomb2_rct,scrn_rct)
        vx2*=yoko
        vy2*=tate
        bomb2_rct.move_ip(vx2,vy2)
        scrn_sfc.blit(bomb2_sfc,bomb2_rct)

        yoko,tate = check_bound_z(bomb3_rct,scrn_rct)
        vx3*=yoko
        vy3*=tate
        bomb3_rct.move_ip(vx3,vy3)
        scrn_sfc.blit(bomb3_sfc,bomb3_rct)

        yoko,tate = check_bound(bomb4_rct,scrn_rct)
        vx4*=yoko
        vy4*=tate
        bomb4_rct.move_ip(vx4,vy4)
        scrn_sfc.blit(bomb4_sfc,bomb4_rct)

        start_time = time.time()

        if tori_rct.colliderect(bomb_rct) or tori_rct.colliderect(bomb2_rct) or tori_rct.colliderect(bomb3_rct):
            stop_time = time.time()
            result = stop_time - start_time
            scrn_sfc.blit(tori2_sfc,tori2_rct)
            text = font.render(f"GAME OVER", True, (255,0,0))# 描画する文字列の設定
            scrn_sfc.blit(text, [scrn_rct.width/2-300, scrn_rct.height/2-10])# 文字列の表示位置
            pg.display.update()
            time.sleep(5)
            return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()