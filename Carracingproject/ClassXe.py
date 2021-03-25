import pygame, random, time, sys
import BuaGame as bg
import MenuGame as Menu

from pygame.locals import *
from pygame import mixer

pygame.init()
WINDOWWIDTH = 1400
WINDOWHEIGHT = 800
BLUE=(0, 180, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (113, 142, 150)
FPS = 60
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

pygame.display.set_caption('GAME DUA XE CA CUOC')
font1 = pygame.font.SysFont('Berlin Sans FB Demi', 50)
font2 = pygame.font.SysFont('Berlin Sans FB Demi', 16)
font3 = pygame.font.SysFont('Berlin Sans FB Demi', 30)


def khoitao(b, c, d, e, f):
    car_Surface1 = pygame.Surface((150, 94), SRCALPHA)
    car_Surface1.blit(pygame.image.load(b), (0, 10))
    car_Surface2 = pygame.Surface((150, 94), SRCALPHA)
    car_Surface2.blit(pygame.image.load(c), (0, 10))
    car_Surface3 = pygame.Surface((150, 94), SRCALPHA)
    car_Surface3.blit(pygame.image.load(d), (0, 10))
    car_Surface4 = pygame.Surface((150, 94), SRCALPHA)
    car_Surface4.blit(pygame.image.load(e), (0, 10))
    car_Surface5 = pygame.Surface((150, 94), SRCALPHA)
    car_Surface5.blit(pygame.image.load(f), (0, 10))
    setcar1 = [car_Surface1, car_Surface2, car_Surface3, car_Surface4, car_Surface5]
    random.shuffle(setcar1)
    return setcar1


namerand = ["John", "Jessica", "Alice", "Jack"]
random.shuffle(namerand)


class Car:
    global nguoichoi
    CarName = ' '
    car_x = 0
    thutucuoigame = 1
    flag = False

    def __init__(self, car_Surface, Vitri):
        self.speedcar = random.randrange(3, 6) + float(random.randrange(1, 100, 30) / 100)
        self.Surface = car_Surface
        self.hieulucbua = False
        self.Car_y = 250 + Vitri * 94
        self.Vitri = Vitri
        self.car_x=40-self.Vitri*20

    def DISPLAY(self, screen):  # hàm vẽ các xe
        screen.blit(self.Surface, (self.car_x, self.Car_y))

    def Name(self, List):
        self.CarName = List[self.Vitri]

    def checkwin(self):  # hàm kiểm tra người thắng
        if self.flag == False:
            self.thutucuoigame = Car.thutucuoigame
            Car.thutucuoigame += 1
            if Car.thutucuoigame == 6:
                Car.thutucuoigame = 1
            self.flag = True


    def RESULT(self, screen):
        if self.thutucuoigame == 1:
            screen.blit(self.Surface, (285, 110))
            return 1
        if self.thutucuoigame == 2:
            screen.blit(self.Surface, (100, 180))
            return 2
        if self.thutucuoigame == 3:
            screen.blit(self.Surface, (460, 190))
            return 3


def RATING(ListCar):
    RattingSurface = pygame.Surface((700, 420), SRCALPHA)
    RattingSurface.blit(pygame.image.load('ratting.png'), (0, 0))
    i=0
    while i<5:
        check=ListCar[i].RESULT(RattingSurface)
        i+=1

    return RattingSurface

def Choose(playername, ListCar):
    while True:
        surf=pygame.Surface((650, 65), pygame.SRCALPHA)
        surf.fill(RED)
        surf.blit(font1.render("Choose your favorite object!!",True,WHITE),(0,0))
        DISPLAYSURF.blit(surf,(375,100))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    Menu.sound("chon.wav",Menu.checksound)
                    pos = pygame.mouse.get_pos()
                    mouse_x = pos[0] // 150
                    mouse_y = (pos[1] - 250) // 96
                    if mouse_x == 0 and mouse_y <= 4 and mouse_y >= 0:
                        a = mouse_y
                        ListCar[a].Surface.blit(font2.render(playername, True, RED, SRCALPHA), (0, 0))
                        return a

        pygame.display.update()


def NameRand(a, playername, namerand, ListCar):
    i = 0
    listname = ["a", "b", "c", "d", "e"]
    while True:
        while i < a:
            ListCar[i].Surface.blit(font2.render(namerand[i], True, WHITE, SRCALPHA), (30, 15))
            listname[i] = namerand[i]
            i = i + 1
        listname[i] = playername
        i = i + 1
        while i > a and i < 5:
            ListCar[i].Surface.blit(font2.render(namerand[i - 1], True, WHITE, SRCALPHA), (30, 15))
            listname[i] = namerand[i - 1]
            i = i + 1
        else:
            break
        pygame.display.update()
    return listname

def ChuanBi(co):
    text_Surface = pygame.Surface((500, 200), SRCALPHA)
    text_Surface.blit(font1.render(' START RACING!! ', True, RED, BLACK), (10, 10))
    while co < 190:
        DISPLAYSURF.blit(text_Surface, (500, 300))
        if co < 60:
            text_Surface.blit(font1.render(' 3 ', True, RED, BLACK), (150, 100))
        elif co >= 60 and co < 120:
            text_Surface.blit(font1.render(' 2 ', True, RED, BLACK), (150, 100))
        elif co >= 120 and co < 180:
            text_Surface.blit(font1.render(' 1 ', True, RED, BLACK), (150, 100))
        else:
            text_Surface.blit(font1.render('GO!!', True, RED, BLACK), (150, 100))
        fpsClock.tick(FPS)
        co = co + 1
        pygame.display.update()
    return co


def Thaydoitoadoxe(ListCar, ListBua, Buaphucloi, WINDOWWIDTH):
    ixe = 0
    while ixe < 10:
        ListBua[ixe].kiemtrabua(ListCar, WINDOWWIDTH)
        ixe += 1
    soxe = 0
    if Buaphucloi != ' ':
        Buaphucloi.kiemtrabua(ListCar, WINDOWWIDTH)
    while soxe < 5:
        ListCar[soxe].car_x += ListCar[soxe].speedcar
        if ListCar[soxe].car_x + 150 > WINDOWWIDTH - soxe*20:
            ListCar[soxe].car_x = WINDOWWIDTH - 150 -soxe*20 
            print(soxe)
            ListCar[soxe].checkwin()
        soxe += 1

def MenuPause():
    Pausesf=pygame.Surface((500,300))
    Pausesf.blit(Menu.nen,(0,0))
    pygame.draw.rect(Pausesf, BLUE, (4, 4, 492, 292), 4)

    Pausesf.blit(font3.render("->PAUSE<-",True,WHITE),(200,10))
    Pausesf.blit(font3.render("Music",True,WHITE),(30,80))
    Pausesf.blit(font3.render("Sound", True, WHITE), (30, 130))
    Pausesf.blit(font3.render("On",True,WHITE),(180,80))
    Pausesf.blit(font3.render("On",True,(WHITE if Menu.checkmusic else BLUE)),(180,130))
    Pausesf.blit(font3.render("Off",True,BLUE),(300,80))
    Pausesf.blit(font3.render("Off",True,(BLUE if Menu.checksound else WHITE)),(300,130))
    Pausesf.blit(font3.render("/",True,BLUE),(270,80))
    Pausesf.blit(font3.render("/",True,BLUE),(270,130))
    Pausesf.blit(font3.render("->>",True,WHITE),(130,200))
    Pausesf.blit(font3.render("<<-",True,WHITE),(350,200))
    Pausesf.blit(font3.render("QUIT GAME",True,BLUE),(180,200))
    Pausesf.blit(font3.render("<- Back", True, BLUE), (30, 250))
    pygame.draw.rect(Pausesf,WHITE,(27,250,120,40),4)
    DISPLAYSURF.blit(Pausesf, (450, 300))
    pygame.display.update()
    checkm=0
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] >450+ 180 - 10 and pos[0] <450+ 180 + 70 and pos[1] >300+ 80  and pos[1] <300+ 80 + 30:
                    Pausesf.blit(font3.render("On", True, WHITE), (180, 80))
                    checkm = 1
                elif pos[0] > 450+300 - 10 and pos[0] < 450+300 + 70 and pos[1] > 300+ 80  and pos[1] <300+ 80 + 30:
                    Pausesf.blit(font3.render("Off", True, WHITE), (300, 80))
                    checkm = 2
                elif pos[0] >450+ 180 - 10 and pos[0] <450+ 180 + 70 and pos[1] >300+ 130  and pos[1] <300+ 130 + 30:
                    Pausesf.blit(font3.render("On", True, WHITE), (180, 130))
                    checkm = 3
                elif pos[0] >450+ 300 -10 and pos[0] <450+ 300 + 70 and pos[1] >300+ 130  and pos[1] <300+ 130 + 30:
                    Pausesf.blit(font3.render("Off", True, WHITE), (300, 130))
                    checkm = 4
                elif pos[0] >450+ 30 and pos[0] <450+ 30+100 and pos[1] >300+ 250 and pos[1] <300+ 300:
                    Pausesf.blit(font3.render("<- Back", True, WHITE), (30, 250))
                    checkm = 5
                elif pos[0] >450+ 180 -10 and pos[0] <450+ 180+200 and pos[1] >300+ 200  and pos[1] <300+ 200+50:
                    Pausesf.blit(font3.render("QUIT GAME", True, WHITE), (180, 200))
                    checkm =6
                else:
                    Pausesf.blit(font3.render("<- Back", True, BLUE), (30, 250))
                    Pausesf.blit(font3.render("QUIT GAME", True, BLUE), (200 - 20, 200))
                    checkm = 0
                    if Menu.checkmusic:
                        Pausesf.blit(font3.render("On", True, WHITE), (180, 80))
                        Pausesf.blit(font3.render("Off", True, BLUE), (300, 80))
                    else:
                        Pausesf.blit(font3.render("On", True, BLUE), (180, 80))
                        Pausesf.blit(font3.render("Off", True, WHITE), (300, 80))
                    if Menu.checksound:
                        Pausesf.blit(font3.render("On", True, WHITE), (180, 130))
                        Pausesf.blit(font3.render("Off", True, BLUE), (300, 130))
                    else:
                        Pausesf.blit(font3.render("On", True, BLUE), (180, 130))
                        Pausesf.blit(font3.render("Off", True, WHITE), (300, 130))
            DISPLAYSURF.blit(Pausesf,(450,300))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    Menu.sound("chon.wav",Menu.checksound)
                    if checkm == 1:
                        Menu.music("dua.mp3", Menu.checksound)
                        Menu.checkmusic = True
                    elif checkm == 2:
                        pygame.mixer.music.unload()
                        Menu.checkmusic = False
                    elif checkm == 3:
                        Menu.checksound=True
                    elif checkm == 4:
                        Menu.checksound=False
                    elif checkm == 5:
                        return 0
                    elif checkm==6:
                        if AsktoQuit()==1:
                            return 1
                        else: continue

def AsktoQuit():
    mcheck = 0
    Pauseasksf = pygame.Surface((500, 300))
    Pauseasksf.blit(Menu.nen,(0,0))
    pygame.draw.rect(Pauseasksf, BLUE, (4, 4, 492, 292), 4)
    Pauseasksf.blit(font3.render("You will lose all your betting money,",True,WHITE),(10,80))
    Pauseasksf.blit(font3.render("do you really want to quit ???",True,WHITE),(30,130))
    Pauseasksf.blit(font3.render("YES",True,BLUE),(150,200))
    Pauseasksf.blit(font3.render("NO",True,BLUE),(300,200))
    pygame.draw.rect(Pauseasksf,WHITE,(130,190,80,50),4)
    pygame.draw.rect(Pauseasksf,WHITE,(280,190,80,50),4)
    DISPLAYSURF.blit(Pauseasksf, (450, 300))
    pygame.display.update()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 450 + 150 and pos[0] < 450 + 150 + 50 and pos[1] > 300 + 200 - 10 and pos[1] < 300 + 200 + 50:
                    Pauseasksf.blit(font3.render("YES", True, GREEN), (150, 200))
                    mcheck = 1
                elif pos[0] > 450 + 300 and pos[0] < 450 + 300 + 50 and pos[1] > 300 + 200 - 10 and pos[1] < 300 + 200 + 50:
                    Pauseasksf.blit(font3.render("NO", True, GREEN), (300, 200))
                    mcheck = 2
                else:
                    mcheck = 0
                    Pauseasksf.blit(font3.render("YES", True, GREY), (150, 200))
                    Pauseasksf.blit(font3.render("NO", True, GREY), (300, 200))
                DISPLAYSURF.blit(Pauseasksf, (450, 300))
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    Menu.sound("chon.wav",Menu.checksound)
                    if mcheck == 1:
                        return 1
                    elif mcheck == 2:
                        return 2



def NewGame(lis, player, lisPhucloi):
    print(lisPhucloi)
    co = 0
    nguoichoi=0
    name = False
    listbua = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 5, 6]
    bua = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    i = 0
    Buaphucloi = ' '
    setcar = khoitao(lis[0], lis[1], lis[2], lis[3], lis[4])
    while i < 10:
        loaibua = random.choice(listbua)
        bua_x = random.randrange(200, 1050)
        if i < 2:
            bua[i] = 250
        elif i < 4:
            bua[i] = 350
        elif i < 6:
            bua[i] = 450
        elif i < 8:
            bua[i] = 550
        else:
            bua[i] = 650
        bua[i] = bg.BuaGame(bua_x, bua[i], loaibua)
        i = i + 1
    CAR = [' ', ' ', ' ', ' ', ' ']
    xe = 0
    while xe < 5:
        CAR[xe] = Car(setcar[xe], xe)
        xe += 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    Menu.sound("chon.wav",Menu.checksound)
                    pos = pygame.mouse.get_pos()
                    if pos[0] > 1310 and pos[0] < 1310 + 80 and pos[1] > 10 and pos[1] < 10 + 80:
                        giu=MenuPause()
                        if giu==0: break
                        elif giu==1: return 5
        DISPLAYSURF.blit(pygame.image.load(lis[5]), (0, 0))
        DISPLAYSURF.blit(pygame.image.load('PBUT.png'), (1310, 10))
        DISPLAYSURF.blit(pygame.image.load('money.png'), (1050, 20))
        DISPLAYSURF.blit(font3.render(str(player.Tiendaugame) + " vnd", True, WHITE, SRCALPHA),(1110, 35))
        CAR[0].DISPLAY(DISPLAYSURF)
        CAR[1].DISPLAY(DISPLAYSURF)
        CAR[2].DISPLAY(DISPLAYSURF)
        CAR[3].DISPLAY(DISPLAYSURF)
        CAR[4].DISPLAY(DISPLAYSURF)
        if name == False:
            nguoichoi = Choose(player.Name, CAR)
            listname = NameRand(nguoichoi, player.Name, namerand, CAR)
            CAR[0].Name(listname)
            CAR[1].Name(listname)
            CAR[2].Name(listname)
            CAR[3].Name(listname)
            CAR[4].Name(listname)
            if lisPhucloi[0] == -1:
                Buaphucloi = bg.BuaGame(160, 250 + 100 * nguoichoi, lisPhucloi[1])
            name = True
            Menu.music("dua.mp3", Menu.checkmusic)
        # cho dòng bắt đầu đua dừng lại 3 dây:
        co = ChuanBi(co)
        a = 0
        while a < 10:
            STT = (bua[a].TDBua_y - 250) // 94
            if CAR[STT].car_x + 150 <= bua[a].TDBua_x:
                bua[a].VeBua(DISPLAYSURF, CAR[STT].car_x)
            else:
                pass
            a = a + 1
        if Buaphucloi != ' ':
            Buaphucloi.VeBua(DISPLAYSURF, CAR[nguoichoi].car_x)
        Thaydoitoadoxe(CAR, bua, Buaphucloi, WINDOWWIDTH)
        if CAR[0].flag and CAR[1].flag and CAR[2].flag and CAR[3].flag and CAR[4].flag:
            break
        pygame.display.update()
        fpsClock.tick(FPS)
    if CAR[nguoichoi].thutucuoigame==1 or CAR[nguoichoi].thutucuoigame==2:
        pygame.mixer.music.unload()
        Menu.music("win.mp3", Menu.checkmusic,1)
        DISPLAYSURF.blit(pygame.image.load("winner.png"),(260,100))
    else:
        pygame.mixer.music.unload()
        Menu.music("lose.mp3", Menu.checkmusic,1)
        DISPLAYSURF.blit(pygame.image.load("loser.png"),(260,100))
    pygame.display.update()
    click=True
    while (click):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    Menu.sound("chon.wav", Menu.checksound)
                    click = False
    DISPLAYSURF.blit(RATING(CAR), (350, 190))
    if CAR[nguoichoi].thutucuoigame==1 or CAR[nguoichoi].thutucuoigame==2:
        pygame.mixer.music.unload()
        Menu.music("win.mp3", Menu.checkmusic,1)
    else:
        pygame.mixer.music.unload()
        Menu.music("lose.mp3", Menu.checkmusic,1)
    pygame.display.update()
    fpsClock.tick(FPS)
    return CAR[nguoichoi].thutucuoigame
