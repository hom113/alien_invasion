import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

from update_screen import update_screen
def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')
    ship = Ship(ai_settings,screen)
    bullets=Group()   



    #开始游戏的主循环
    while True:
    #监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bullets)
        update_screen(screen,ship,ai_settings,bullets)

run_game()