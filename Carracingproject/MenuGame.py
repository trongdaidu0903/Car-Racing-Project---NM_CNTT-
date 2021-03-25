import pygame, random, sys
import ClassXe as clxe
import Minigame
from pygame.locals import *
from pygame import mixer
from datetime import datetime
pygame.init()
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
GREY=(113, 142, 150)
BLUE=(0, 180, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

WINDOWWIDTH = 1400
WINDOWHEIGHT = 800
MENUSURFACE = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

font2 = pygame.font.SysFont('Berlin Sans FB Demi', 20)
font3 = pygame.font.SysFont('Berlin Sans FB Demi', 25)
font4 = pygame.font.SysFont('Berlin Sans FB Demi', 35)

# menuchinh
hcn0 = pygame.Surface((250, 50), pygame.SRCALPHA)
#pygame.draw.rect(hcn0, BLUE, (2, 2, 242, 42), 4)
hcn1 = pygame.Surface.copy(hcn0)
hcn2 = pygame.Surface.copy(hcn0)
hcn3 = pygame.Surface.copy(hcn0)
hcn4 = pygame.Surface.copy(hcn0)
hcn5 = pygame.Surface.copy(hcn0)
select = ["NEW GAME", "INSTRUCTION", "HISTORY", "SETTINGS", "ABOUT", "EXIT", "Log In", "Sign Up", "Log Out" ]
long=[9,10.5,7,7,6,4]
HCN = [hcn0, hcn1, hcn2, hcn3, hcn4, hcn5]
height = WINDOWHEIGHT / 2
BG=pygame.image.load("backgr.png")
nen=pygame.image.load("nenn.png")

# exit
exitsf = pygame.Surface((500, 160))
exitsf.blit(nen,(0,0))
pygame.draw.rect(exitsf, BLUE, (4, 4, 492, 152), 4)
exitsf.blit(font3.render("DO YOU WANT TO EXIT:", True, WHITE), (40, 20))
exitsf.blit(font3.render("YES", True, BLUE), (100, 90))
exitsf.blit(font3.render("NO", True, BLUE), (350, 90))
pygame.draw.rect(exitsf,WHITE,(80,85,90,40),4)
pygame.draw.rect(exitsf,WHITE,(330,85,90,40),4)

# settings
onsf1 = pygame.Surface((40, 40),pygame.SRCALPHA)
offsf1 = pygame.Surface.copy(onsf1)
onsf1.blit(font3.render("On", True, WHITE), (0, 0))
offsf1.blit(font3.render("Off", True, BLUE), (0, 0))
onsf2 = pygame.Surface.copy(onsf1)
offsf2 = pygame.Surface.copy(offsf1)
checksound = True
checkmusic= True

def scale(bg):
    bg=pygame.transform.scale(bg,(1400,800))
    MENUSURFACE.blit(bg,(0,0))

def InPutText(screen, title, Nguoichoi1):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    text = ""
    mmpos = -1
    SurfaceIPN = pygame.Surface((500, 300), SRCALPHA)
    SurfaceIPN.blit(nen,(0,0))
    pygame.draw.rect(SurfaceIPN, BLUE, (0, 0, 500, 300), 4)
    pygame.draw.rect(SurfaceIPN, WHITE, (70, 195, 100, 40), 4)
    pygame.draw.rect(SurfaceIPN, WHITE, (335, 195, 100, 40), 4)
    SurfaceIPN.blit(font3.render(title, True, WHITE), (40, 20))
    SurfaceIPN.blit(font3.render("OK", True, BLUE), (100, 200))
    SurfaceIPN.blit(font3.render("Cancle", True, BLUE), (350, 200))
    text_surf = pygame.Surface((300, 40), SRCALPHA)
    text_surf.fill(BLUE)
    SurfaceIPN.blit(text_surf, (100, 100))
    pygame.display.update()
    while (1):
        screen.blit(SurfaceIPN, (450, 250))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 550 and pos[0] < 600 and pos[1] > 250 + 200 and pos[1] < 250 + 200 + 30:
                    SurfaceIPN.blit(font3.render("OK", True, WHITE), (100, 200))
                    screen.blit(SurfaceIPN, (450, 250))
                    mmpos=0
                elif pos[0] > 800 and pos[0] < 950 and pos[1] > 250 + 200 and pos[1] < 250 + 200 + 30:
                    SurfaceIPN.blit(font3.render("Cancle", True, WHITE), (350, 200))
                    screen.blit(SurfaceIPN, (450, 250))
                    mmpos=1
                else:
                    SurfaceIPN.blit(font3.render("OK", True, BLUE), (100, 200))
                    SurfaceIPN.blit(font3.render("Cancle", True, BLUE), (350, 200))
                    screen.blit(SurfaceIPN, (450, 250))
                    mmpos = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if mmpos==0:
                        return text
                    elif mmpos==1:
                        scale(nen)
                        Change(9,True, Nguoichoi1)
                        return 0
            elif event.type == pygame.KEYDOWN:
                if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                    text += event.unicode
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                if event.key == pygame.K_RETURN:
                    return text
            text_surf.fill(BLUE)
            text_surf.blit(font3.render(text, True, WHITE), (0, 0))
            SurfaceIPN.blit(text_surf, (100, 100))
            pygame.display.flip()

def LogSign(screen, title, text):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    IDname = ""
    IDflash=True
    Password =""
    PasswordOut =""
    mmpos = -1
    SurfaceIPN = pygame.Surface((700, 400), SRCALPHA)
    SurfaceIPN.blit(nen,(0,0))
    pygame.draw.rect(SurfaceIPN, BLUE, (0, 0, 700, 400), 4)
    pygame.draw.rect(SurfaceIPN, WHITE, (100, 300, 100, 40), 4)
    pygame.draw.rect(SurfaceIPN, WHITE, (500, 300, 100, 40), 4)
    SurfaceIPN.blit(font3.render(title, True, WHITE), (40, 20))
    SurfaceIPN.blit(font3.render("OK", True, BLUE), (130, 306))
    SurfaceIPN.blit(font3.render("Cancle", True, BLUE), (515, 305))
    text_surf1 = pygame.Surface((300, 40), SRCALPHA)
    text_surf1.fill(BLUE)
    text_surf2=pygame.Surface.copy(text_surf1)
    SurfaceIPN.blit(font3.render("ID      :", True, BLUE), (100, 125))
    SurfaceIPN.blit(font3.render("Password:", True, BLUE), (100, 200))
    SurfaceIPN.blit(text_surf1, (300, 125))
    SurfaceIPN.blit(font3.render(text, True, WHITE), (300, 160))
    SurfaceIPN.blit(text_surf2, (300, 200))
    pygame.display.update()
    while (1):
        screen.blit(SurfaceIPN, (350, 200))
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 450 and pos[0] < 550 and pos[1] > 500 and pos[1] < 540:
                    SurfaceIPN.blit(font3.render("OK", True, WHITE), (130, 306))
                    screen.blit(SurfaceIPN, (350, 200))
                    mmpos=0
                elif pos[0] > 850 and pos[0] < 950 and pos[1] > 500 and pos[1] < 540:
                    SurfaceIPN.blit(font3.render("Cancle", True, WHITE), (515, 305))
                    screen.blit(SurfaceIPN, (350, 200))
                    mmpos=1
                else:
                    SurfaceIPN.blit(font3.render("OK", True, BLUE), (130, 306))
                    SurfaceIPN.blit(font3.render("Cancle", True, BLUE), (515, 305))
                    screen.blit(SurfaceIPN, (350, 200))
                    mmpos = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if mmpos==0:
                        if IDname.find(" ")==-1 and len(Password)>=6:
                            lis=[True, IDname, Password]
                            return lis
                        else:
                            return [False]
                    elif mmpos==1:
                        return [False]
                    elif pos[0] > 650 and pos[0] < 750 and pos[1] > 400 and pos[1] < 440:
                    	IDflash=False
            elif event.type == pygame.KEYDOWN:
                if IDflash==True:
                    if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        IDname += event.unicode
                    elif event.key == pygame.K_BACKSPACE:
                        IDname = IDname[:-1]
                    elif event.key == pygame.K_RETURN:
                        IDflash=False
                elif IDflash==False:
                    if event.key != pygame.K_RETURN and event.key != pygame.K_BACKSPACE:
                        Password += event.unicode
                        PasswordOut+='*'
                    elif event.key == pygame.K_BACKSPACE:
                        Password = Password[:-1]
                        PasswordOut=PasswordOut[:-1]
                    elif event.key == pygame.K_RETURN:
                        if IDname.find(" ")==-1 and len(Password)>=6:
                            lis=[True, IDname, Password]
                            return lis
                        else:
                            return [False]

            if IDflash==True:
                text_surf1.fill(WHITE)
                text_surf1.blit(font3.render(IDname, True, BLUE), (0, 0))
                SurfaceIPN.blit(text_surf1, (300, 125))
                text_surf1.fill(BLUE)
                text_surf1.blit(font3.render(PasswordOut, True, WHITE), (0, 0))
                SurfaceIPN.blit(text_surf2, (300, 200))
                pygame.display.flip()
            elif IDflash==False:
                text_surf1.fill(BLUE)
                text_surf1.blit(font3.render(IDname, True, WHITE), (0, 0))
                SurfaceIPN.blit(text_surf1, (300, 125))
                text_surf2.fill(WHITE)
                text_surf2.blit(font3.render(PasswordOut, True, BLUE), (0, 0))
                SurfaceIPN.blit(text_surf2, (300, 200))
                pygame.display.flip()


def Change(i, dangnhap, Nguoichoi1):
    MENUSURFACE.blit(pygame.image.load('money.png'), (850, 20))
    MENUSURFACE.blit(font3.render(str(Nguoichoi1.Tiendaugame) + " vnd", True, WHITE, SRCALPHA), (910, 35))
    if i == 9:
        t = 0
        while t < 6:
            HCN[t].blit(font3.render(select[t], True, BLUE), (250/2-15*long[t]/2, 5))
            MENUSURFACE.blit(HCN[t], (WINDOWWIDTH / 2 - 250 / 2, WINDOWHEIGHT / 2 + t * 58))
            t = t + 1
        if dangnhap==False:
            MENUSURFACE.blit(font3.render("Log In", True, BLUE), (1200, 35))
            MENUSURFACE.blit(font3.render("Sign Up", True, BLUE), (1200, 70))
        else:
            MENUSURFACE.blit(font3.render("Welcome " + Nguoichoi1.Name, True, BLUE), (1200, 35))
            MENUSURFACE.blit(font3.render("Log Out", True, BLUE), (1200, 70))
    elif i<6:
        HCN[i].blit(font3.render(select[i], True, WHITE), (250/2-15*long[i]/2, 0))
        MENUSURFACE.blit(HCN[i], [WINDOWWIDTH / 2 - 250 / 2, WINDOWHEIGHT / 2 + i * 58])
    else:
        if dangnhap==False:
            if i<8:
                MENUSURFACE.blit(font3.render(select[i], True, WHITE), (1200, 33+(i-6)*35))
        else:
            MENUSURFACE.blit(font3.render(select[8], True, WHITE), (1200, 33+35))
    pygame.display.update()

def sound(url, check):  # Âm thanh
    if check:
        pygame.mixer.Sound.play(pygame.mixer.Sound("chon.wav"))

def music(url,check,x=0):
    if check and x==1:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(url)
        pygame.mixer.music.play(0, 0, 0)
    elif check:
        pygame.mixer.music.unload()
        pygame.mixer.music.load(url)
        pygame.mixer.music.play(-100,0,0)

def exit():
    mmpos = -1
    MENUSURFACE.blit(exitsf, (450, 300))
    pygame.display.update()
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 550 and pos[0] < 600 and pos[1] > 300 + 90 and pos[1] < 300 + 90 + 40:
                    exitsf.blit(font3.render("YES", True, WHITE), (100, 90))
                    MENUSURFACE.blit(exitsf, (450, 300))
                    mmpos = 0
                elif pos[0] > 800 and pos[0] < 850 and pos[1] > 300 + 90 and pos[1] < 300 + 90 + 40:
                    exitsf.blit(font3.render("NO", True, WHITE), (350, 90))
                    MENUSURFACE.blit(exitsf, (450, 300))
                    mmpos = 1
                else:
                    exitsf.blit(font3.render("YES", True, BLUE), (100, 90))
                    exitsf.blit(font3.render("NO", True, BLUE), (350, 90))
                    MENUSURFACE.blit(exitsf, (450, 300))
                    mmpos = 2
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if mmpos == 0:
                        pygame.quit()
                        sys.exit()
                    elif mmpos == 1:
                        return
            pygame.display.update()

def BacktoMenu(dangnhap, Nguoichoi1):
    MENUSURFACE.blit(BG,(0,0))
    Change(9, dangnhap, Nguoichoi1)
    pygame.display.update()

class Nguoichoi:
    def __init__(self,Name,tien):
        self.Name = Name
        self.Tiendaugame=tien
        self.tiencuoc=0

def Game(nguoichoi, phucloi, fileSave):
    lis = NewGame(nguoichoi)
    if lis!=1:
        tiencuoc = InPutText(MENUSURFACE, "Money want to bet (at least 50000vnd):", nguoichoi)
    else:
        BacktoMenu(True,nguoichoi)
        return
    if tiencuoc == 0:
        pass
    else:
        while tiencuoc.isdigit() == False or int(tiencuoc) < 50000 or int(tiencuoc) > nguoichoi.Tiendaugame:
            tiencuoc = InPutText(MENUSURFACE, "Money want to bet (at least 50000vnd):", nguoichoi)
    tiencuoc = int(tiencuoc)
    if tiencuoc == 0:
        BacktoMenu(True,nguoichoi)
    else:
        nguoichoi.tiencuoc=tiencuoc
        check = KiemTraThangThua(lis, nguoichoi, nguoichoi.Tiendaugame, nguoichoi.tiencuoc, phucloi, fileSave)
        if len(check) == 2:
            phucloi = check
            return phucloi
        else:
            phucloi=check
            nguoichoi.Tiendaugame = check[0]
            return phucloi

def Menu():
    Nguoichoi1=Nguoichoi('You', 0)
    dangnhap = False
    nhapten=False
    fileSave=' '
    MENUSURFACE.blit(BG,(0,0))
    mpos = -1
    dem = 0
    global map
    while (dem < 9):
        Change(dem, False, Nguoichoi1)
        dem = dem + 1
    Change(9, False, Nguoichoi1)
    phucloi = [0]
    music("xoso.mp3",checkmusic)
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > WINDOWWIDTH / 2 - 250 / 2 and pos[0] < WINDOWWIDTH / 2 + 250 / 2:
                    if pos[1] > height + 0 * 58 and pos[1] < height + 0 * 60 + 58:
                        Change(0,dangnhap, Nguoichoi1)
                        mpos = 1
                    elif pos[1] > height + 1 * 58 and pos[1] < height + 1 * 58 + 50:
                        Change(1,dangnhap, Nguoichoi1)
                        mpos = 2
                    elif pos[1] > height + 2 * 58 and pos[1] < height + 2 * 58 + 50:
                        Change(2,dangnhap, Nguoichoi1)
                        mpos = 3
                    elif pos[1] > height + 3 * 58 and pos[1] < height + 3 * 58 + 50:
                        Change(3,dangnhap, Nguoichoi1)
                        mpos = 4
                    elif pos[1] > height + 4 * 58 and pos[1] < height + 4 * 58 + 50:
                        Change(4,dangnhap, Nguoichoi1)
                        mpos = 5
                    elif pos[1] > height + 5 * 58 and pos[1] < height + 5 * 58 + 50:
                        Change(5,dangnhap, Nguoichoi1)
                        mpos = 6
                    else:
                        Change(9,dangnhap, Nguoichoi1)
                        mpos = 0
                elif pos[0]>1200 and pos[0]<1300:
                    if pos[1]>35 and pos[1]<60:
                        if dangnhap==False:
                            Change(6, False, Nguoichoi1)
                            mpos = 7
                    elif pos[1]>70 and pos[1]<95:
                        if dangnhap==False:
                            Change(7, False,Nguoichoi1)
                            mpos = 8
                        elif dangnhap==True:
                            Change(8, True, Nguoichoi1)
                            mpos = 9
                else:
                    Change(9,dangnhap, Nguoichoi1)
                    mpos = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if mpos == 1:
                        if dangnhap==False:
                            surf1 = pygame.Surface((600, 100), pygame.SRCALPHA)
                            surf1.blit(nen,(0,0))
                            surf1.blit(font4.render("You must Log In or Sign Up.", True, WHITE), (10, 30))
                            BacktoMenu(dangnhap,Nguoichoi1)
                            MENUSURFACE.blit(surf1, (400, 350))
                            pygame.display.update()
                            click=True
                            while (click):
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if pygame.mouse.get_pressed()[0]:
                                            sound("chon.wav", checksound)
                                            BacktoMenu(False,Nguoichoi1)
                                            click = False
                        elif dangnhap==True and Nguoichoi1.Name=='You':
                            if nhapten == False:
                                Nguoichoi1.Name=InPutText(MENUSURFACE, "Input Your Name:", Nguoichoi1)
                                if Nguoichoi1.Name == 0:
                                    BacktoMenu(True,Nguoichoi1)
                                else:
                                    nhapten = True
                                    click = True
                                    surf = pygame.Surface((600, 100), pygame.SRCALPHA)
                                    surf.blit(nen,(0,0))
                                    surf.blit(font4.render("You have been received 500000vnd.", True, WHITE), (10, 30))
                                    BacktoMenu(dangnhap,Nguoichoi1)
                                    MENUSURFACE.blit(surf, (400, 350))
                                    pygame.display.update()
                                    while (click):
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if pygame.mouse.get_pressed()[0]:
                                                    sound("chon.wav", checksound)
                                                    click = False
                                    phucloi=Game(Nguoichoi1, phucloi, fileSave)
                            else:
                                phucloi= Game(Nguoichoi1, phucloi, fileSave)
                        else:
                            if Nguoichoi1.Tiendaugame>50000:
                                phucloi= Game(Nguoichoi1, phucloi, fileSave)
                                music("xoso.mp3",checkmusic)
                            else:
                                surf1 = pygame.Surface((600, 200), pygame.SRCALPHA)
                                surf1.blit(nen,(0,0))
                                surf1.blit(font4.render("You don't have enough money, Play minigame:", True, WHITE), (10, 30))
                                BacktoMenu(dangnhap,Nguoichoi1)
                                MENUSURFACE.blit(surf1, (400, 300))
                                pygame.display.update()
                                click=True
                                while (click):
                                    for event in pygame.event.get():
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            if pygame.mouse.get_pressed()[0]:
                                                sound("chon.wav", checksound)
                                                click = False
                                                Nguoichoi1.Tiendaugame=Minigame.playMinigame(Nguoichoi1.Tiendaugame)
                                                BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos == 2:
                        Instruction()
                        BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos == 3:
                        if dangnhap==True:
                            History(fileSave)
                        BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos == 4:
                        Settings(checkmusic,checksound)
                        BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos == 5:
                        About()
                        BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos == 6:
                        exit()
                        BacktoMenu(dangnhap,Nguoichoi1)
                    elif mpos ==7:
                        A=DangNhap(Nguoichoi1)
                        dangnhap=A[0]
                        if dangnhap==True:
                        	Nguoichoi1=Nguoichoi(A[1],A[2])
                        	fileSave=A[3]+".txt"
                    elif mpos ==8:
                        A=DangKi(Nguoichoi1)
                        dangnhap=A[0]
                        if dangnhap==True:
                        	Nguoichoi1=Nguoichoi(A[1],A[2])
                        	fileSave=A[3]+".txt"
                    elif mpos == 9:
                        LogOut(fileSave, Nguoichoi1)
                        dangnhap=False
                        nhapten=False
                        fileSave=' '
                        Nguoichoi1=Nguoichoi('You', 0)
                        BacktoMenu(False,Nguoichoi1)
                    else:
                        break

def KiemTraThangThua(lis, Nguoichoi1, tien, tiencuoc, phucloi, fileSave):
    f=open(fileSave)
    A=f.readline()
    f.close()
    f=open(fileSave,'a+')
    if lis == 1:
        pass
    else:
        now = datetime.now()
        check = clxe.NewGame(lis, Nguoichoi1, phucloi)
    if check == 1:
        sound("win.mp3",checkmusic)
        tien = tien + tiencuoc
        f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc)+ "vnd and take the first place, his/her money: "+ str(tien)+'\n')
    elif check == 2:
        sound("win.mp3",checkmusic)
        choose = ChooseOption()
        if choose == -1:
            tien = tien + int(0.5 * tiencuoc)
            f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc)+ "vnd and take the second place, his/her money: "+ str(tien)+'\n')
        else:
            AAA = [-1, choose]
            BacktoMenu(True,Nguoichoi1)
            f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc)+ "vnd and take the second place, his/her money: "+ str(tien)+'\n')
            f.close()
            return AAA
    elif check == 3:
        f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc) + "vnd and take the third place, his/her money: "+ str(tien)+'\n')
        sound("lose.mp3", checkmusic)
    elif check == 4:
        sound("lose.mp3", checkmusic)
        tien = tien - int(0.5 * tiencuoc)
        f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc)+ "vnd and take the fourth place, his/her money: "+ str(tien)+'\n')
    elif check == 5:
        sound("lose.mp3", checkmusic)
        tien = tien - tiencuoc
        f.write(now.strftime("%d/%m/%Y %H:%M:%S")+", "+ Nguoichoi1.Name + " have been betted " +  str(tiencuoc)+ "vnd and take the last place, his/her money: "+ str(tien)+'\n')
    A = [tien]
    click = True
    while (click):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    BacktoMenu(True,Nguoichoi1)
                    click = False
    f.close()
    return A

def Newgameblit(bg):
    MENUSURFACE.blit(bg[0], (150, 200))
    MENUSURFACE.blit(bg[1], (550, 200))
    MENUSURFACE.blit(bg[2], (950, 200))
    MENUSURFACE.blit(bg[3], (300, 450))
    MENUSURFACE.blit(bg[4], (800, 450))

def initBG(B):
    bg1 = pygame.Surface((1400, 800), pygame.SRCALPHA)
    pygame.draw.rect(bg1, BLUE, (0, 0, 1390, 790), 10)
    bg2 = pygame.Surface.copy(bg1)
    bg3 = pygame.Surface.copy(bg1)
    bg4 = pygame.Surface.copy(bg1)
    bg5 = pygame.Surface.copy(bg1)
    bg1.blit(pygame.image.load(B[0]), (0, 0))
    bg2.blit(pygame.image.load(B[1]), (0, 0))
    bg3.blit(pygame.image.load(B[2]), (0, 0))
    bg4.blit(pygame.image.load(B[3]), (0, 0))
    bg5.blit(pygame.image.load(B[4]), (0, 0))
    bg1 = pygame.transform.scale(bg1, (300, 200))
    bg2 = pygame.transform.scale(bg2, (300, 200))
    bg3 = pygame.transform.scale(bg3, (300, 200))
    bg4 = pygame.transform.scale(bg4, (300, 200))
    bg5 = pygame.transform.scale(bg5, (300, 200))
    bg = [bg1, bg2, bg3, bg4, bg5]
    return bg

def NewGame(Nguoichoi1):
    scale(nen)
    ibg = ['bg1.png', 'bg2.png', 'bg3.png', 'bg4.png', 'bg5.png']
    bg = initBG(ibg)
    Newgameblit(bg)
    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
    pygame.draw.rect(MENUSURFACE, WHITE, (90, 690, 120, 50), 4)
    MENUSURFACE.blit(font4.render("Welcome " + Nguoichoi1.Name + ", Choose map:", True, WHITE), (WINDOWWIDTH / 2 - 300, 100))
    pygame.display.update()
    mpos = -1
    dem=0
    while dem < 5:
        pygame.draw.rect(bg[dem], BLUE, (2, 2, 296, 196), 5)
        dem = dem + 1
    Newgameblit(bg)
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 150 and pos[0] < 150 + 300 and pos[1] > 200 and pos[1] < 200 + 200:
                    pygame.draw.rect(bg[0], WHITE, (2, 2, 296, 196), 5)
                    MENUSURFACE.blit(bg[0], (150, 200))
                    mpos = 0
                elif pos[0] > 550 and pos[0] < 550 + 300 and pos[1] > 200 and pos[1] < 200 + 200:
                    pygame.draw.rect(bg[1], WHITE, (2, 2, 296, 196), 5)
                    MENUSURFACE.blit(bg[1], (550, 200))
                    mpos = 1
                elif pos[0] > 950 and pos[0] < 950 + 300 and pos[1] > 200 and pos[1] < 200 + 200:
                    pygame.draw.rect(bg[2], WHITE, (2, 2, 296, 196), 5)
                    MENUSURFACE.blit(bg[2], (950, 200))
                    mpos = 2
                elif pos[0] > 300 and pos[0] < 300 + 300 and pos[1] > 450 and pos[1] < 450 + 200:
                    pygame.draw.rect(bg[3], WHITE, (2, 2, 296, 196), 5)
                    MENUSURFACE.blit(bg[3], (300, 450))
                    mpos = 3
                elif pos[0] > 800 and pos[0] < 800 + 300 and pos[1] > 450 and pos[1] < 450 + 200:
                    pygame.draw.rect(bg[4], WHITE, (2, 2, 296, 196), 5)
                    MENUSURFACE.blit(bg[4], (800, 450))
                    mpos = 4
                elif pos[0] > 80 and pos[0] < 200 and pos[1] > 650 and pos[1] < 750:
                    MENUSURFACE.blit(font3.render("<- Back", True, WHITE), (100, 700))
                    mpos = 5
                else:
                    mpos = -1
                    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
                    dem = 0
                    while dem < 5:
                        pygame.draw.rect(bg[dem], BLUE, (2, 2, 296, 196), 5)
                        dem = dem + 1
                    Newgameblit(bg)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if mpos == 0:
                        lis = ['S11.png', 'S12.png', 'S13.png', 'S14.png', 'S15.png', ibg[0]]
                        return lis
                    elif mpos == 1:
                        lis = ['S21.png', 'S22.png', 'S23.png', 'S24.png', 'S25.png', ibg[1]]
                        return lis
                    elif mpos == 2:
                        lis = ['S31.png', 'S32.png', 'S33.png', 'S34.png', 'S35.png', ibg[2]]
                        return lis
                    elif mpos == 3:
                        lis = ['S41.png', 'S42.png', 'S43.png', 'S44.png', 'S45.png', ibg[3]]
                        return lis
                    elif mpos == 4:
                        lis = ['S51.png', 'S52.png', 'S53.png', 'S54.png', 'S55.png', ibg[4]]
                        return lis
                    elif mpos == 5:
                        scale(nen)
                        Change(9, True, Nguoichoi1)
                        return 1
            pygame.display.update()

def Back():
    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
    pygame.draw.rect(MENUSURFACE,WHITE,(90,690,120,50),4)
    pygame.display.update()
    checkb = False
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 80 and pos[0] < 200 and pos[1] > 700 and pos[1] < 730:
                    MENUSURFACE.blit(font3.render("<- Back", True, WHITE), (100, 700))
                    checkb = True
                else:
                    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
                    checkb = False
                pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if checkb == True:
                        return True

def About():
    scale(nen)
    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
    pygame.draw.rect(MENUSURFACE, WHITE, (90, 690, 120, 50), 4)
    MENUSURFACE.blit(font3.render("DO AN NHAP MON CONG NGHE THONG TIN", True, WHITE), (100, 100))
    MENUSURFACE.blit(font3.render("20CTT3", True, WHITE), (100, 200))
    MENUSURFACE.blit(font3.render("Nhom 7", True, WHITE), (100, 250))
    MENUSURFACE.blit(font3.render("20120409   -   Tran Thanh Tung", True, WHITE), (100, 300))
    MENUSURFACE.blit(font3.render("20120435   -   Le Thi Ngoc Bich", True, WHITE), (100, 340))
    MENUSURFACE.blit(font3.render("20120442   -   Nguyen Huu Chinh", True, WHITE), (100, 380))
    MENUSURFACE.blit(font3.render("20120449   -   Tran Trong Dai", True, WHITE), (100, 420))
    MENUSURFACE.blit(font3.render("20120452   -   Dinh Viet Danh", True, WHITE), (100, 460))
    MENUSURFACE.blit(font3.render("Giao vien huong dan: ThS. Vo Hoang Quan", True, WHITE), (100, 520))
    pygame.display.update()
    Back()

def Settings(checkmusic,checksound):
    scale(nen)
    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
    pygame.draw.rect(MENUSURFACE, WHITE, (90, 690, 120, 50), 4)
    MENUSURFACE.blit(font4.render("->SETTINGS<-", True, WHITE), (WINDOWWIDTH / 2 - 100, 100))
    MENUSURFACE.blit(font4.render("Music", True, WHITE), (200, 200))
    MENUSURFACE.blit(font4.render("Sound", True, WHITE), (200, 300))
    MENUSURFACE.blit(onsf1, (400, 200 + 7))
    MENUSURFACE.blit(offsf1, (400 + 100, 200 + 7))
    MENUSURFACE.blit(font3.render("/", True, BLUE), (400 + 70, 200 + 7))
    MENUSURFACE.blit(onsf2, (400, 300 + 7))
    MENUSURFACE.blit(offsf2, (400 + 100, 300 + 7))
    MENUSURFACE.blit(font3.render("/", True, BLUE), (400 + 70, 300 + 7))
    pygame.display.update()
    checkm = 0
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if pos[0] > 400 - 10 and pos[0] < 400 + 70 and pos[1] > 200 - 10 and pos[1] < 200 + 40:
                    onsf1.blit(font3.render("On", True, WHITE), (0, 0))
                    offsf1.blit(font3.render("Off", True, BLUE), (0, 0))
                    checkm = 1
                elif pos[0] > 400 + 70 and pos[0] < 400 + 70 + 80 and pos[1] > 200 - 10 and pos[1] < 200 + 40:
                    offsf1.blit(font3.render("Off", True, WHITE), (0, 0))
                    onsf1.blit(font3.render("On", True, BLUE), (0, 0))
                    checkm = 2
                elif pos[0] > 400 - 10 and pos[0] < 400 + 70 and pos[1] > 300 - 10 and pos[1] < 300 + 40:
                    onsf2.blit(font3.render("On", True, WHITE), (0, 0))
                    offsf2.blit(font3.render("Off", True, BLUE), (0, 0))
                    checkm = 3
                elif pos[0] > 400 + 70 and pos[0] < 400 + 70 + 80 and pos[1] > 300 - 10 and pos[1] < 300 + 40:
                    onsf2.blit(font3.render("On", True, BLUE), (0, 0))
                    offsf2.blit(font3.render("Off", True, WHITE), (0, 0))
                    checkm = 4
                elif pos[0] > 80 and pos[0] < 200 and pos[1] > 650 and pos[1] < 750:
                    MENUSURFACE.blit(font3.render("<- Back", True, WHITE), (100, 700))
                    checkm = 5
                else:
                    MENUSURFACE.blit(font3.render("<- Back", True, BLUE), (100, 700))
                    checkm = 0
                    if checkmusic:
                        onsf1.blit(font3.render("On", True, WHITE), (0, 0))
                        offsf1.blit(font3.render("Off", True, BLUE), (0, 0))
                    else:
                        onsf1.blit(font3.render("On", True, BLUE), (0, 0))
                        offsf1.blit(font3.render("Off", True, WHITE), (0, 0))
                    if checksound:
                        offsf2.blit(font3.render("Off", True, BLUE), (0, 0))
                        onsf2.blit(font3.render("On", True, WHITE), (0, 0))
                    else:
                        offsf2.blit(font3.render("Off", True, WHITE), (0, 0))
                        onsf2.blit(font3.render("On", True, BLUE), (0, 0))
            MENUSURFACE.blit(onsf1, (400, 200 + 7))
            MENUSURFACE.blit(offsf1, (400 + 100, 200 + 7))
            MENUSURFACE.blit(onsf2, (400, 300 + 7))
            MENUSURFACE.blit(offsf2, (400 + 100, 300 + 7))
            pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    sound("chon.wav", checksound)
                    if checkm == 1:
                        music("xoso.mp3",checkmusic)
                        checkmusic = True
                    elif checkm == 2:
                        pygame.mixer.music.unload()
                        checkmusic = False
                    elif checkm == 3:
                        checksound = True
                    elif checkm == 4:
                        checksound = False
                    elif checkm == 5:
                        return

def History(stri):
    scale(nen)
    MENUSURFACE.blit(font4.render("->HISTORY<-", True, WHITE), (WINDOWWIDTH / 2 - 100, 100))
    a=open(stri)
    lines=a.readlines()
    a.close()
    j=len(lines)
    if j<10:
        while j>1:
            MENUSURFACE.blit(font3.render(lines[j-1], True, WHITE), (50,80+ 40*j))
            j-=1
    else:
        i=0
        while i<15:
            MENUSURFACE.blit(font3.render(lines[j-1], True, WHITE), (50,80+ 40*i))
            j-=1
            i+=1
    pygame.display.update()
    Back()

def Instruction():
    scale(nen)
    MENUSURFACE.blit(font4.render("->INSTRUCTION<-", True, WHITE), (WINDOWWIDTH / 2 - 130, 100))
    MENUSURFACE.blit(font3.render("Welcome to SPEED BET, relax yourself by immensing into world of speed, race and win, conquer the topmost level",True, WHITE), (70, 150))
    MENUSURFACE.blit(font3.render("of standings.", True, WHITE), (70, 180))
    MENUSURFACE.blit(font3.render("Step 1 :  For the best game experiencing , we recommend that you should put on your real headphone, because",True, WHITE), (70, 240))
    MENUSURFACE.blit(font3.render("sound and music are combined perfectly to visualize to player best expericence", True, WHITE),(70, 270))
    MENUSURFACE.blit(font3.render("Step 2 : When run the game executable file, you reach to the main menu game , at here, there are 6 options :",True, WHITE), (70, 310))
    MENUSURFACE.blit(font3.render("- “ New game “: Start new game, choose the map , then start racing.", True, WHITE),(70, 340))
    MENUSURFACE.blit(font3.render("- “ Instructions “", True, WHITE), (70, 370))
    MENUSURFACE.blit(font3.render("- “ History “:Your races will be recorded here", True, WHITE), (70, 400))
    MENUSURFACE.blit(font3.render("- “ Settings” : Customize sounds and musics ON/OFF", True, WHITE), (70, 430))
    MENUSURFACE.blit(font3.render("- “Credits” : Information about our team who created this game, our mentor M.S. Vo Hoang Quan",True, WHITE), (70, 460))
    MENUSURFACE.blit(font3.render("- “Exit” : To quit the game.", True, WHITE), (70, 490))
    MENUSURFACE.blit(font3.render("Step 3 : Choose “New game “, next , there are 5 map, choosing your favorite map according to your preference,",True, WHITE), (70, 530))
    MENUSURFACE.blit(font3.render("every map has its own style and theme, cars/bikes as well different from another.", True, WHITE),(70, 560))
    MENUSURFACE.blit(font3.render("Step 4 : Let’s racing, double click on the car you like most among 5 cars/bikes, then go on after 3..2..1",True, WHITE), (70, 600))
    pygame.display.update()
    Back()

def ChooseOption():
    choosesf = pygame.Surface((500, 300))
    choosesf.blit(nen,(0,0))
    pygame.draw.rect(choosesf, BLUE, (4, 4, 492, 292), 4)
    choosesf.blit(font3.render("Choose your gift:", True, WHITE), (40, 20))
    choosesf.blit(font3.render("50% betted money", True, BLUE), (30, 220))
    choosesf.blit(font3.render("A Magic Box", True, BLUE), (300, 220))
    MENUSURFACE.blit(choosesf, (450, 300))
    op1 = pygame.Surface((100, 100), pygame.SRCALPHA)
    pygame.draw.rect(op1, BLUE, (0, 0, 100, 100), 4)
    op2=pygame.Surface.copy(op1)
    op1.blit(pygame.image.load("P50.png"), (0, 0))
    op2.blit(pygame.image.load("HBA1.png"), (0, 0))
    choosesf.blit(op1,(75,100))
    choosesf.blit(op2,(325,100))
    pygame.display.update()
    while (1):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                if (pos[0] > 480 and pos[0] < 700 and pos[1] > 300 + 220 and pos[1] < 300 + 220 + 40) or (pos[0] > 450+75 and pos[0] < 450+175 and pos[1] > 400 and pos[1] < 500):
                    choosesf.blit(font3.render("50% betted money", True, WHITE), (30, 220))
                    pygame.draw.rect(choosesf, WHITE, (75, 100, 100, 100), 4)
                    MENUSURFACE.blit(choosesf, (450, 300))
                elif (pos[0] > 750 and pos[0] < 880 and pos[1] > 300 + 220 and pos[1] < 300 + 220 + 40) or (pos[0] > 450+325 and pos[0] < 450+425 and pos[1] > 400 and pos[1] < 500):
                    choosesf.blit(font3.render("A Magic Box", True, WHITE), (300, 220))
                    pygame.draw.rect(choosesf, WHITE, (325, 100, 100, 100), 4)
                    MENUSURFACE.blit(choosesf, (450, 300))
                else:
                    choosesf.blit(font3.render("50% betted money", True, BLUE), (30, 220))
                    choosesf.blit(font3.render("A Magic Box", True, BLUE), (300, 220))
                    pygame.draw.rect(choosesf, BLUE, (75, 100, 100, 100), 4)
                    pygame.draw.rect(choosesf, BLUE, (325, 100, 100, 100), 4)
                    MENUSURFACE.blit(choosesf, (450, 300))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if (pos[0] > 480 and pos[0] < 700 and pos[1] > 300 + 220 and pos[1] < 300 + 220 + 40) or (pos[0] > 450+75 and pos[0] < 450+175 and pos[1] > 400 and pos[1] < 500):
                        sound("chon.wav", checksound)
                        return -1
                    elif (pos[0] > 750 and pos[0] < 880 and pos[1] > 300 + 220 and pos[1] < 300 + 220 + 40) or (pos[0] > 450+325 and pos[0] < 450+425 and pos[1] > 400 and pos[1] < 500):
                        return random.choice([0, 1, 2, 3, 6])
            pygame.display.update()

def DangKi(Nguoichoi1):
	f=open("DangNhap.txt", 'r')
	Dangki=f.read()
	f.close()
	f=open("DangNhap.txt", 'a+')
	DKlis=LogSign(MENUSURFACE, "Sign Up:", " ")
	pygame.display.update()
	while True:
		if DKlis[0]==1:
			if Dangki.find(DKlis[1]+' ')==-1:
				f.write(DKlis[1]+' '+DKlis[2]+"\n")
				f.close()
				fi=open(DKlis[1]+".txt", mode = "a+")
				fi.write('You'+' '+str(500000)+"\n")
				BacktoMenu(True,Nguoichoi1)
				pygame.display.update()
				return [True,'You',500000, DKlis[1]]
			else:
				DKlis=LogSign(MENUSURFACE, "Sign Up:", "ID have already exist, try again:")
				pygame.display.update()
		else:
			BacktoMenu(False,Nguoichoi1)
			pygame.display.update()
			return [False]

def DangNhap(Nguoichoi1):
    f=open("DangNhap.txt")
    Dangnhap=f.read()
    DNlis=LogSign(MENUSURFACE, "Log in:", " ")
    pygame.display.update()
    check=True
    while (check):
        if DNlis[0]==1:
            if Dangnhap.find(DNlis[1]+' ')!=-1 and Dangnhap.find(DNlis[2]+'\n') == Dangnhap.find(DNlis[1]+' ')+len(DNlis[1])+1 :
                fi=open(DNlis[1]+".txt")
                fi.seek(0)
                a=fi.readline()
                fi.close()
                a=a.split()
                BacktoMenu(True,Nguoichoi1)
                pygame.display.update()
                return [True, a[0], int(a[1]), DNlis[1]]
            else:
                DNlis=LogSign(MENUSURFACE, "Log In:", "ID or Password is incorrect")
                pygame.display.update()
        else:
            BacktoMenu(False,Nguoichoi1)
            pygame.display.update()
            return [False]
def LogOut(fileSave, Nguoichoi1):
	f=open(fileSave, 'r+')
	lines=f.readlines()
	f.seek(0)
	f.write(Nguoichoi1.Name+ ' '+ str(Nguoichoi1.Tiendaugame)+'\n')
	for line in lines:
		if line!= lines[0]:
			f.write(line)
	f.truncate()
	f.close()
	
Menu()
