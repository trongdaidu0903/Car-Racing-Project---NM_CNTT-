import pygame, sys, random, time
from pygame.locals import *

def playMinigame(tien):
	running = True
	def checkMoney(money):
			if money >= 1000:
				font = pygame.font.SysFont('consolas', 30)
				text_report = font.render('Your money is enough, you must to leave minigame !', True, (255, 255, 255))            
				DISPLAYSURF.blit(text_report, (200, 300))
				time.sleep(1)
				running = False
				return running
			running = True
	while running:
		WINDOWWIDTH = 1400
		WINDOWHEIGHT = 800

		X_MARGIN = 80
		LANEWIDTH = 60

		SHIP_WIDTH = 60
		SHIP_HEIGHT = 70

		OBSTACLE_Width = 120
		OBSTACLE_Height = 230

		SHIP_SPEED = 12
		SHIP_IMG = pygame.image.load('ship.png')

		DISTANCE = 200
		OBSTACLESSPEED = 6
		CHANGESPEED = 0.05

		OBSTACLES1 = pygame.image.load('meteo1.png')
		OBSTACLES2 = pygame.image.load('meteo2.png')
		OBSTACLES3 = pygame.image.load('meteo3.png')
		OBSTACLES4 = pygame.image.load('meteo4.png')

		BGSPEED = 6
		BGIMG = pygame.image.load('BG.png')

		pygame.init()

		FPS = 60
		fpsClock = pygame.time.Clock()

		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		pygame.display.set_caption('RACING')

		class Background(): 
		    def __init__(self):
		        self.x = 0
		        self.y = 0
		        self.speed = BGSPEED
		        self.img = BGIMG
		        self.width = self.img.get_width()
		        self.height = self.img.get_height()
		    def draw(self):
		        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y)))
		        DISPLAYSURF.blit(self.img, (int(self.x), int(self.y-self.height)))
		    def update(self):
		        self.y += self.speed
		        if self.y > self.height:
		            self.y -= self.height

		class Obstacles(): 
		    def __init__(self):
		        self.width = OBSTACLE_Width
		        self.height = OBSTACLE_Height
		        self.distance = DISTANCE
		        self.speed = OBSTACLESSPEED
		        self.changeSpeed = CHANGESPEED
		        self.ls = []
		        for i in range(5):
		            y = -OBSTACLE_Height-i*self.distance
		            lane = random.randint(0, 20)
		            self.ls.append([lane, y])
		    def draw(self):
		        
		        for i in range(5):
		            x = int(X_MARGIN + self.ls[i][0]*LANEWIDTH + (LANEWIDTH-self.width)/2)
		            y = int(self.ls[i][1])
		            OBSTACLESIMG = random.choice([OBSTACLES1, OBSTACLES2, OBSTACLES3, OBSTACLES4])
		            DISPLAYSURF.blit(OBSTACLESIMG, (x, y))
		    def update(self):
		        for i in range(5):
		            self.ls[i][1] += self.speed
		        self.speed += self.changeSpeed
		        if self.ls[0][1] > WINDOWHEIGHT:
		            self.ls.pop(0)
		            y = self.ls[3][1] - self.distance
		            lane = random.randint(0, 20)
		            self.ls.append([lane, y])

		class Car():
		    def __init__(self):
		        self.width = SHIP_WIDTH
		        self.height = SHIP_HEIGHT
		        self.x = (WINDOWWIDTH-self.width)/2
		        self.y = (WINDOWHEIGHT-self.height)/2
		        self.speed = SHIP_SPEED
		        self.surface = pygame.Surface((self.width, self.height))
		        self.surface.fill((255, 255, 255))
		    def draw(self):
		        DISPLAYSURF.blit(SHIP_IMG, (int(self.x), int(self.y)))
		    def update(self, moveLeft, moveRight, moveUp, moveDown):
		        if moveLeft == True:
		            self.x -= self.speed 
		        if moveRight == True:
		            self.x += self.speed 
		        if moveUp == True:
		            self.y -= self.speed
		        if moveDown == True:
		            self.y += self.speed + 6

		        if self.x < X_MARGIN:
		            self.x = X_MARGIN
		        if self.x + self.width > WINDOWWIDTH - X_MARGIN:
		            self.x = WINDOWWIDTH - X_MARGIN - self.width
		        if self.y < 0:
		            self.y = 0
		        if self.y + self.height > WINDOWHEIGHT:
		            self.y = WINDOWHEIGHT - self.height

		class Score():
		    totalMoney=0
		    def __init__(self):
		        self.score = 0
		        self.money = 0
		    def draw(self):
		        font = pygame.font.SysFont('consolas', 50)
		        scoreSuface = font.render('Score: '+str(int(self.score)), True, (255, 255, 255))
		        DISPLAYSURF.blit(scoreSuface, (20, 10))
		        moneySurface = font.render('Money: ' +str(int(self.money)), True, (255, 255, 255))
		        DISPLAYSURF.blit(moneySurface, (20, 50))

		        font2 = pygame.font.SysFont('consolas', 30)
		        tutorial_text1 = font2.render('Press UP, DOWN, LEFT, RIGHT', True, (255, 255, 255))
		        tutorial_text2 = font2.render('to control the Ship', True, (255, 255, 255))
		        DISPLAYSURF.blit(tutorial_text1, (910, 30))
		        DISPLAYSURF.blit(tutorial_text2, (960, 70))
		    def update(self):
		        self.score += 0.2
		        self.money = self.score * 100
		        Score.totalMoney = self.score * 100
		        return Score.totalMoney

		def rectCollision(rect1, rect2):
		    if rect1[0] <= rect2[0]+rect2[2] and rect2[0] <= rect1[0]+rect1[2] and rect1[1] <= rect2[1]+rect2[3] and rect2[1] <= rect1[1]+rect1[3]:
		        return True
		    return False

		def isGameover(car, obstacles):
		    carRect = [car.x, car.y, car.width, car.height]
		    for i in range(5):
		        x = int(X_MARGIN + obstacles.ls[i][0]*LANEWIDTH + (LANEWIDTH-obstacles.width)/2)
		        y = int(obstacles.ls[i][1])
		        obstaclesRect = [x, y, obstacles.width, obstacles.height]
		        if rectCollision(carRect, obstaclesRect) == True:
		            return True
		    return False

		def gameStart(bg):
		    bg.__init__()
		    font = pygame.font.SysFont('consolas', 200)
		    headingSuface = font.render('SPACE SHIP', True, (255, 0, 0))
		    headingSize = headingSuface.get_size()

		    font = pygame.font.SysFont('consolas', 60)
		    commentSuface = font.render('Press "SPACE" to play', True, (255, 255, 255))
		    commentSize = commentSuface.get_size()
		    while True:
		        for event in pygame.event.get():
		            if event.type == pygame.QUIT:
		                pygame.quit()
		                sys.exit()
		            if event.type == pygame.KEYUP:
		                if event.key == K_SPACE:
		                    return
		        bg.draw()
		        DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 200))
		        DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 450))
		        pygame.display.update()
		        fpsClock.tick(FPS)

		def gamePlay(bg, car, obstacles, score):
		    car.__init__()
		    obstacles.__init__()
		    bg.__init__()
		    score.__init__()
		    moveLeft = False
		    moveRight = False
		    moveUp = False
		    moveDown = False
		    while True:
		        for event in pygame.event.get():
		            if event.type == pygame.QUIT:
		                pygame.quit()
		                sys.exit()
		            if event.type == KEYDOWN:
		                if event.key == K_LEFT:
		                    moveLeft = True
		                if event.key == K_RIGHT:
		                    moveRight = True
		                if event.key == K_UP:
		                    moveUp = True
		                if event.key == K_DOWN:
		                    moveDown = True
		            if event.type == KEYUP:
		                if event.key == K_LEFT:
		                    moveLeft = False
		                if event.key == K_RIGHT:
		                    moveRight = False
		                if event.key == K_UP:
		                    moveUp = False
		                if event.key == K_DOWN:
		                    moveDown = False
		        if isGameover(car, obstacles):
		            return MN
		        bg.draw()
		        bg.update()
		        car.draw()
		        car.update(moveLeft, moveRight, moveUp, moveDown)
		        obstacles.draw()
		        obstacles.update()
		        Score()
		        score.draw()
		        MN=score.update()	
		        pygame.display.update()
		        fpsClock.tick(FPS)

		def gameOver(bg, car, obstacles, score):
		    font = pygame.font.SysFont('consolas', 200)
		    headingSuface = font.render('GAMEOVER', True, (255, 0, 0))
		    headingSize = headingSuface.get_size()

		    font = pygame.font.SysFont('consolas', 60)
		    commentSuface = font.render('Press "space" to replay', True, (255, 255, 255))
		    commentSize = commentSuface.get_size()
		    while True:
		        for event in pygame.event.get():
		            if event.type == pygame.QUIT:
		                pygame.quit()
		                sys.exit()
		            if event.type == pygame.KEYUP:
		                if event.key == K_SPACE:
		                    return
		        bg.draw()
		        car.draw()
		        obstacles.draw()
		        score.draw()
		        DISPLAYSURF.blit(headingSuface, (int((WINDOWWIDTH - headingSize[0])/2), 200))
		        DISPLAYSURF.blit(commentSuface, (int((WINDOWWIDTH - commentSize[0])/2), 450))
		        pygame.display.update()
		        fpsClock.tick(FPS)


		def gamemini(tien):
		    bg = Background()
		    car = Car()
		    obstacles = Obstacles()
		    score = Score()
		    gameStart(bg)
		    while tien<50000:
		        A=gamePlay(bg, car, obstacles, score)
		        gameOver(bg, car, obstacles, score)
		        print(A)
		       	tien +=A
		       	print(tien)
		    return tien
		
		tien = gamemini(tien)
		return tien

