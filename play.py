#coding=utf-8

import pygame
import time
from pygame.locals import *

def main():
    
    #1. 创建窗口
    screen = pygame.display.set_mode((480,500),0,32)#852 -> 500
    #2. 获取背景图
    background = pygame.image.load("./feiji/background.png")
    # 获取飞机图
    hero = pygame.image.load("./feiji/hero1.png")
    # 记录飞机的位置 
    x = 210
    y = 400
    #3. 加载背景图
    while True:
        # 显示背景
        screen.blit(background,(0,0))
        # 显示飞机
        screen.blit(hero,(x,y))
        #4. 需要刷新才显示图片
        pygame.display.update()   
        #模拟移动
        #x += 1
        #y -= 1
		#获取事件，比如按键等
        for event in pygame.event.get():

            #判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            #判断是否是按下了键
            elif event.type == KEYDOWN:
                #检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    x-=5
                #检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x+=5
                #检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')


        time. sleep(0.01)
if __name__ == "__main__":
    main()



