#coding=utf-8

import pygame
import time
from pygame.locals import *
class HeroPlane(object):
	def __init__(self,screen_temp):
		self.x = 210
		self.y = 700
		self.image =  pygame.image.load("./feiji/hero1.png")
		self.screen = screen_temp
		self.bullet_list=[]
	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x +=5

	def display(self):
		self.screen.blit(self.image,(self.x,self.y))
		for bullet in self.bullet_list:#有一颗子弹，显示一颗，并移动出去永无休止
			bullet.display()
			bullet.move()

	def fire(self):
        	self.bullet_list.append(Bullet(self.screen,self.x,self.y)) #通过这里创建的子弹

class Bullet(object) :  
	def __init__(self,screen_temp,x,y):
		self.x = x + 40 
		self.y = y - 20
		self.image =  pygame.image.load("./feiji/bullet.png")
		self.screen = screen_temp #必须显示出来才有用

	def display(self):
		'''子弹必须显示才能看见  '''
		self.screen.blit(self.image,(self.x,self.y))
	
	def move(self):
		self.y -= 10

def key_control(hero_temp):
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
				hero_temp.move_left()
			#检测按键是否是d或者right
			elif event.key == K_d or event.key == K_RIGHT:
				print('right')
				hero_temp.move_right()
			#检测按键是否是空格键
			elif event.key == K_SPACE:
				print('space')
				hero_temp.fire()


def main():
    
    #1. 创建窗口
    screen = pygame.display.set_mode((480,852),0,32)#852 -> 500
    #2. 获取背景图
    background = pygame.image.load("./feiji/background.png")
    # 获取飞机对象
    hero = HeroPlane(screen)
	#3. 加载背景图
    while True:
        # 显示背景
        screen.blit(background,(0,0))
        # 显示飞机
        hero.display()
		#4. 需要刷新才显示图片
        pygame.display.update()   
		#获取事件，比如按键等
        key_control(hero)
        time. sleep(0.01)
if __name__ == "__main__":
    main()



