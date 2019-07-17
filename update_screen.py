import pygame

def update_screen(screen,ship,ai_settings,bullets):
    """更新屏幕背景颜色、飞船以及游戏屏幕绘制"""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
        #把ship传过去
    ship.blileme()
    #让最近绘制的屏幕可见
    pygame.display.flip()