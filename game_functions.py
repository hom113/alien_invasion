import sys
import pygame
from bullet import Bullet

def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    if event.key==pygame.K_UP:
        ship.moving_up=True
    if event.key==pygame.K_DOWN:
        ship.moving_down=True
    elif event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
        
def fire_bullet(ai_settings,screen,ship,bullets):
     #创建一颗子弹，并将其加入到编组bullets中
     if(len(bullets)<ai_settings.bullets_allowed):
         new_bullet= Bullet(ai_settings,screen,ship)
         bullets.add(new_bullet)
        
        
def check_keyup_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    if event.key==pygame.K_UP:
        ship.moving_up=False
    if event.key==pygame.K_DOWN:
        ship.moving_down=False    


def check_events(ai_settings,screen,ship,bullets):
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ai_settings,screen,ship,bullets)
            
            
def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    #更新子弹的位置
    bullets.update()
    
    #删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <=0:
            bullets.remove(bullet)