import pygame as pg
import random
import MenuGame as Menu
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
pg.init()
listbua=[0,1,2,3]
loaibua = random.choice(listbua)
bua_x=random.randrange(300, 1200)
class BuaGame:
	hieuluc=0
	flagsound = [1, 1, 1, 1, 1, 1, 1]
	def __init__(self, x, y, loaibua):
		self.TDBua_x=x
		self.TDBua_y=y
		self.Loaibua=loaibua
		self.flag= False
		self.lane=(y-250)//94 #vi tri lane ma bua nam tren do.
	def VeBua(self,screen,car_x):
		if self.Loaibua != -1:
			if self.TDBua_x-car_x<175:
				if self.Loaibua==0:
					screen.blit(pg.image.load('B0.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==1:		
					screen.blit(pg.image.load('B1.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==2:		
					screen.blit(pg.image.load('B2.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==3:		
					screen.blit(pg.image.load('B3.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==4:		
					screen.blit(pg.image.load('B4.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==5:		
					screen.blit(pg.image.load('B5.png'), (self.TDBua_x, self.TDBua_y))
				elif self.Loaibua==6:		
					screen.blit(pg.image.load('B6.png'), (self.TDBua_x, self.TDBua_y))
			else:
				screen.blit(pg.image.load('HBA1.png'), (self.TDBua_x, self.TDBua_y))
	def BuaNhanh(self, carclass):
			carclass[self.lane].car_x+=carclass[self.lane].speedcar
	def BuaCham(self, carclass):
			carclass[self.lane].car_x-=0.5*carclass[self.lane].speedcar
	def BuaDungYen(self, carclass):
			carclass[self.lane].car_x-=carclass[self.lane].speedcar
	def BuaLui(self, carclass):
			carclass[self.lane].car_x-=1.5*carclass[self.lane].speedcar
	def BuaQuayVeVitriXP(self, carclass):
			carclass[self.lane].car_x=0
	def BuaDichChuyen(self, carclass):
			carclass[self.lane].car_x+=150
	def BuaVeDich(self, carclass, WINDOWWIDTH):
			carclass[self.lane].car_x=WINDOWWIDTH
	def kiemtrabua(self,carclass,WINDOWWIDTH):
		if carclass[self.lane].car_x+150>self.TDBua_x and self.flag==False:
			self.hieuluc=30
			self.flag=True
		if self.Loaibua==0 and self.hieuluc>0:
			SOUND("tangtoc.wav",0,Menu.checkmusic)
			self.BuaNhanh(carclass)
			self.hieuluc=self.hieuluc-1
			if self.hieuluc==0:
				self.Loaibua=-1
				BuaGame.flagsound[0]=1
		elif self.Loaibua==1 and self.hieuluc>0:
			SOUND("cham.wav",1,Menu.checkmusic)
			self.BuaCham(carclass)
			self.hieuluc=self.hieuluc-1
			if self.hieuluc==0:
				self.Loaibua=-1
				BuaGame.flagsound[1]=1
		elif self.Loaibua==2 and self.hieuluc>0:
			SOUND("dunglai.wav",2,Menu.checkmusic)
			self.BuaDungYen(carclass)
			self.hieuluc=self.hieuluc-1
			if self.hieuluc==0:
				self.Loaibua=-1
				BuaGame.flagsound[2]=1
		elif self.Loaibua==3 and self.hieuluc>0:
			SOUND("dichlui.wav",3,Menu.checkmusic)
			if self.hieuluc==30:
				carclass[self.lane].Surface=FLIP_IMG(carclass[self.lane].Surface)
			self.BuaLui(carclass)
			self.hieuluc=self.hieuluc-1
			if self.hieuluc==0:
				carclass[self.lane].Surface=FLIP_IMG(carclass[self.lane].Surface)
				BuaGame.flagsound[3]=1
				self.Loaibua=-1
		elif self.Loaibua==4 and self.hieuluc>0:
			SOUND("chacchet.mp3",4,Menu.checkmusic)
			self.BuaQuayVeVitriXP(carclass)
			self.hieuluc=0
			if self.hieuluc==0:
				BuaGame.flagsound[4]=1
				self.Loaibua=-1
		elif self.Loaibua==5 and self.hieuluc>0:
			SOUND("dichtoi.wav",5,Menu.checkmusic)
			self.BuaDichChuyen(carclass)
			self.hieuluc=0
			if self.hieuluc==0:
				BuaGame.flagsound[5]=1
				self.Loaibua=-1
		elif self.Loaibua==6 and self.hieuluc>0:
			SOUND("vedich.mp3",6,Menu.checkmusic)
			self.BuaVeDich(carclass, WINDOWWIDTH)
			return 0
def FLIP_IMG(image):
	image = pg.transform.flip(image, True, False)
	return image
def SOUND(url,i,checksound):
	if checksound and BuaGame.flagsound[i]:
		pg.mixer.Sound.play(pg.mixer.Sound(url))
		BuaGame.flagsound[i]=0
