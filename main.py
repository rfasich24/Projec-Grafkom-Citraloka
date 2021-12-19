#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT.freeglut import *

#Kotak yang berisi cerita
def Cerita_1():
    judul = "PERISTIWA RENGASDENGKLOK"
    glColor3f(0,0,0)
    glRasterPos( 700+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(600+pos_x,900)
    glVertex2f(600+pos_x,700)
    glVertex2f(1200+pos_x,700)
    glVertex2f(1200+pos_x,900)
    glEnd()
    for i in judul:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))


def Cerita_2():
    LatarBelakang = "Latar Belakang:"
    poin_1 ="- Jepang kalah pada Perang Dunia 2"
    poin_2 ="- Lalu terjadi Kekosongan Kekuasaan"
    poin_3 ="- Berujung pada pertentangan antara Golongan Tua dan Muda"
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(2200+pos_x,650)
    glVertex2f(2200+pos_x,900)
    glVertex2f(3100+pos_x,900)
    glVertex2f(3100+pos_x,650)
    glEnd()
    glColor3f(0,0,0)
    glRasterPos( 2300+pos_x,850)
    for i in LatarBelakang:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos(2300+pos_x,800)
    for i in poin_1:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos(2300+pos_x,750)
    for i in poin_2:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos(2300+pos_x,700)
    for i in poin_3:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))


def Cerita_3():
    kronologi = "Kronologi Kejadian"
    glColor3f(0,0,0)
    glRasterPos( 4600+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(4400+pos_x,700)
    glVertex2f(4400+pos_x,900)
    glVertex2f(5000+pos_x,900)
    glVertex2f(5000+pos_x,700)
    glEnd()
    for i in kronologi:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))


def Cerita_4():
    tanggal = "15 Agustus 2945"
    peristiwa_1 = "- Peristiwa diawali dengan Pertemuan di Lembaga Bakteriologi oleh golongan muda"
    peristiwa_2 = "- Dilanjutkan dengan pertemuan golongan tua & muda di kediaman Ir. Soekarno"
    peristiwa_3 = "- Terjadi Kesalah Pahaman antara Wikana dan Ir. Soekarno yang membuat Soekarno marah pada golongan muda"
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(6000+pos_x,650)
    glVertex2f(6000+pos_x,900)
    glVertex2f(7500+pos_x,900)
    glVertex2f(7500+pos_x,650)
    glEnd()
    glColor3f(0,0,0)
    glRasterPos( 6600+pos_x,850)
    for i in tanggal:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 6100+pos_x,800)
    for i in peristiwa_1:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 6100+pos_x,750)
    for i in peristiwa_2:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 6100+pos_x,700)
    for i in peristiwa_3:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    

def Cerita_5():
    tanggal = "16 Agustus 1945"
    peristiwa_1 = "- Perbedaan pendapat membuat golongan muda membawa Soekarno-Hatta ke Rengasdengklok agar jauh dari jepang/sekutu"
    peristiwa_2 = "- Golongan muda memaksa Soekarno-Hatta merumuskan Proklamasi"
    peristiwa_3 = "- Achmad Soebardjo Berjanji pada golongan muda proklamasi akan dilaksanakan jika Soekarno-Hatta dikembalikan ke Jakarta"
    peristiwa_4 = "- Soekarno mengungkapkan rencana proklamasi dilaksanakaan pada tanggal 17 Agustus"
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(7950+pos_x,600)
    glVertex2f(7950+pos_x,900)
    glVertex2f(9500+pos_x,900)
    glVertex2f(9500+pos_x,600)
    glEnd()
    glColor3f(0,0,0)
    glRasterPos( 8600+pos_x,850)
    for i in tanggal:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 8000+pos_x,800)
    for i in peristiwa_1:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 8000+pos_x,750)
    for i in peristiwa_2:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 8000+pos_x,700)
    for i in peristiwa_3:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 8000+pos_x,650)
    for i in peristiwa_4:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))


def Cerita_6():
    tanggal = "17 Agustus 1945"
    ending = "Akhirnya Proklamasi berhasil diadakan pada tanggal 17 Agustus 1945 di Jakarta"
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(9950+pos_x,700)
    glVertex2f(9950+pos_x,850)
    glVertex2f(10950+pos_x,850)
    glVertex2f(10950+pos_x,700)
    glEnd()
    glColor3f(0,0,0)
    glRasterPos( 10350+pos_x,800)
    for i in tanggal:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))
    glRasterPos( 10000+pos_x,750)
    for i in ending:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

def canyon():
    glBegin(GL_QUADS)
    glColor3ub(0,255,255)
    glVertex2f(1000+pos_x,0)
    glVertex2f(1000+pos_x,100)
    glVertex2f(1500+pos_x,100)
    glVertex2f(1500+pos_x,0)

    glVertex2f(2500+pos_x,0)
    glVertex2f(2500+pos_x,100)
    glVertex2f(2800+pos_x,100)
    glVertex2f(2800+pos_x,0)

    glVertex2f(4500+pos_x,0)
    glVertex2f(4500+pos_x,100)
    glVertex2f(4800+pos_x,100)
    glVertex2f(4800+pos_x,0)

    glVertex2f(6000+pos_x,0)
    glVertex2f(6000+pos_x,100)
    glVertex2f(6550+pos_x,100)
    glVertex2f(6550+pos_x,0)

    glVertex2f(7500+pos_x,0)
    glVertex2f(7500+pos_x,100)
    glVertex2f(8000+pos_x,100)
    glVertex2f(8000+pos_x,0)
    glEnd()

#Objek-Objek
def tanah():
    glBegin(GL_POLYGON) 
    glColor3ub(128,0,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,100)
    glVertex2f(13000+pos_x,100)
    glVertex2f(13000+pos_x,0)
    glEnd()

def karakter():
    global ulang, jump, isjumping
    # glScaled(2,2,0)
    if ulang == True :
        ulang = False
        isjumping = False
        jump = 0
        glTranslated(100,80+jump,0)
    else :
        glTranslated(100,80+jump,0)
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(80,180)
    glVertex2f(80,30)
    glVertex2f(230,30)
    glVertex2f(230,180)

    glColor3ub(92,35,11)
    glVertex2f(90,90)
    glVertex2f(90,30)
    glVertex2f(220,30)
    glVertex2f(220,90)

    glColor3ub(41,32,30)
    glVertex2f(90,50)
    glVertex2f(90,30)
    glVertex2f(220,30)
    glVertex2f(220,50)

    glColor3ub(244,202,155)
    glVertex2f(120,150)
    glVertex2f(200,150)
    glVertex2f(200,100)
    glVertex2f(120,100)
    
    glVertex2f(110,140)
    glVertex2f(210,140)
    glVertex2f(210,110)
    glVertex2f(110,110)

#outline
    glColor3ub(50,50,50)
    glVertex2f(90,20)
    glVertex2f(120,20)
    glVertex2f(120,30)
    glVertex2f(90,30)

    glVertex2f(80,70)
    glVertex2f(90,70)
    glVertex2f(90,30)
    glVertex2f(80,30)

    glVertex2f(70,70)
    glVertex2f(70,110)
    glVertex2f(80,110)
    glVertex2f(80,70)

    glVertex2f(80,110)
    glVertex2f(90,110)
    glVertex2f(90,200)
    glVertex2f(80,200)

    glVertex2f(80,190)
    glVertex2f(80,200)
    glVertex2f(70,200)
    glVertex2f(70,190)

    glVertex2f(90,190)
    glVertex2f(110,190)
    glVertex2f(110,180)
    glVertex2f(90,180)

    glVertex2f(110,180)
    glVertex2f(110,170)
    glVertex2f(200,170)
    glVertex2f(200,180)

    glVertex2f(200,190)
    glVertex2f(200,180)
    glVertex2f(220,180)
    glVertex2f(220,190)

    glVertex2f(220,110)
    glVertex2f(230,110)
    glVertex2f(230,200)
    glVertex2f(220,200)

    glVertex2f(230,200)
    glVertex2f(240,200)
    glVertex2f(240,190)
    glVertex2f(230,190)

    glVertex2f(220,200)
    glVertex2f(220,210)
    glVertex2f(200,210)
    glVertex2f(200,200)

    glVertex2f(200,220)
    glVertex2f(200,210)
    glVertex2f(180,210)
    glVertex2f(180,220)

    glVertex2f(180,230)
    glVertex2f(180,220)
    glVertex2f(130,220)
    glVertex2f(130,230)

    glVertex2f(130,210)
    glVertex2f(130,220)
    glVertex2f(110,220)
    glVertex2f(110,210)

    glVertex2f(110, 210)
    glVertex2f(110,200)
    glVertex2f(90,200)
    glVertex2f(90,210)

    glVertex2f(240,110)
    glVertex2f(230,110)
    glVertex2f(230,70)
    glVertex2f(240,70)

    glVertex2f(230,70)
    glVertex2f(220,70)
    glVertex2f(220,30)
    glVertex2f(230,30)

    glVertex2f(220,30)
    glVertex2f(190,30)
    glVertex2f(190,20)
    glVertex2f(220,20)

    glVertex2f(190,40)
    glVertex2f(120,40)
    glVertex2f(120,30)
    glVertex2f(190,30)

    glColor3ub(84,148,82)
    glVertex2f(90,110)
    glVertex2f(100,110)
    glVertex2f(100,70)
    glVertex2f(90,70)
    
    glVertex2f(90,110)
    glVertex2f(90,100)
    glVertex2f(80,100)
    glVertex2f(80,110)

    glVertex2f(210,110)
    glVertex2f(220,110)
    glVertex2f(220,70)
    glVertex2f(210,70)

    glVertex2f(220,110)
    glVertex2f(230,110)
    glVertex2f(230,100)
    glVertex2f(220,100)

    glColor3ub(0,0,0)
    glVertex2f(130,130)
    glVertex2f(140,130)
    glVertex2f(140,120)
    glVertex2f(130,120)

    glVertex2f(190,130)
    glVertex2f(200,130)
    glVertex2f(200,120)
    glVertex2f(190,120)

    glVertex2f(150,120)
    glVertex2f(180,120)
    glVertex2f(180,110)
    glVertex2f(150,110)

    #kepala
    glColor3ub(58,19,4)
    glVertex2f(110,210)
    glVertex2f(200,210)
    glVertex2f(200,180)
    glVertex2f(110,180)

    glVertex2f(90,200)
    glVertex2f(220,200)
    glVertex2f(220,190)
    glVertex2f(90,190)

    glVertex2f(130,220)
    glVertex2f(180,220)
    glVertex2f(180,210)
    glVertex2f(130,210)

    glEnd()

def TiangBendera():
    glBegin(GL_QUADS)
    glColor3ub(0,0,0)
    glVertex2f(11400+pos_x,800)
    glVertex2f(11400+pos_x,100)
    glVertex2f(11350+pos_x,100)
    glVertex2f(11350+pos_x,800)
    glEnd()

def BenderaMerah():
    glBegin(GL_QUADS)
    glColor3ub(255,0,0)
    glVertex2f(11350+pos_x,800)
    glVertex2f(11100+pos_x,800)
    glVertex2f(11100+pos_x,700)
    glVertex2f(11350+pos_x,700)
    glEnd()

def BenderaPutih():
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(11350+pos_x,700)
    glVertex2f(11350+pos_x,600)
    glVertex2f(11100+pos_x,600)
    glVertex2f(11100+pos_x,700)
    glEnd()

def Awan():
    glBegin(GL_QUADS)
    glColor3ub(175,162,255)
    glVertex2f(1850+pos_x,600)
    glVertex2f(1850+pos_x,650)
    glVertex2f(2150+pos_x,650)
    glVertex2f(2150+pos_x,600)

    glVertex2f(1900+pos_x,650)
    glVertex2f(1900+pos_x,700)
    glVertex2f(2100+pos_x,700)
    glVertex2f(2100+pos_x,650)

    glVertex2f(2000+pos_x,700)
    glVertex2f(2000+pos_x,750)
    glVertex2f(2050+pos_x,750)
    glVertex2f(2050+pos_x,700) 
    glEnd()

def Awan2():
    glBegin(GL_QUADS)
    glColor3ub(175,162,255)
    glVertex2f(2950+pos_x,500)
    glVertex2f(2950+pos_x,550)
    glVertex2f(3150+pos_x,550)
    glVertex2f(3150+pos_x,500)

    glVertex2f(3050+pos_x,550)
    glVertex2f(3050+pos_x,600)
    glVertex2f(3100+pos_x,600)
    glVertex2f(3100+pos_x,550)

    glVertex2f(3350+pos_x,850)
    glVertex2f(3350+pos_x,900)
    glVertex2f(3450+pos_x,900)
    glVertex2f(3450+pos_x,850)

    glVertex2f(3450+pos_x,550)
    glVertex2f(3450+pos_x,600)
    glVertex2f(3500+pos_x,600)
    glVertex2f(3500+pos_x,550) 
    glEnd()

def Awan3():
    glBegin(GL_QUADS)
    glColor3ub(175,162,255)
    glVertex2f(3800+pos_x,650)
    glVertex2f(3800+pos_x,750)
    glVertex2f(4100+pos_x,750)
    glVertex2f(4100+pos_x,650)

    glVertex2f(3850+pos_x,750)
    glVertex2f(3850+pos_x,800)
    glVertex2f(3950+pos_x,800)
    glVertex2f(3950+pos_x,750)

    glVertex2f(4000+pos_x,650)
    glVertex2f(4000+pos_x,600) 
    glVertex2f(3850+pos_x,600)
    glVertex2f(3850+pos_x,650)
    glEnd()

def Awan4():
    glBegin(GL_QUADS)
    glColor3ub(175,162,255)
    glVertex2f(4500+pos_x,500)
    glVertex2f(4500+pos_x,550)
    glVertex2f(4800+pos_x,550)
    glVertex2f(4800+pos_x,500)

    glVertex2f(4600+pos_x,500)
    glVertex2f(4600+pos_x,600)
    glVertex2f(4800+pos_x,600)
    glVertex2f(4800+pos_x,500)

    glVertex2f(4650+pos_x,450)
    glVertex2f(4650+pos_x,500)
    glVertex2f(4700+pos_x,500)
    glVertex2f(4700+pos_x,450)
#opsi
    glVertex2f(5250+pos_x,500)
    glVertex2f(5250+pos_x,550)
    glVertex2f(5400+pos_x,550)
    glVertex2f(5400+pos_x,500) 

    glVertex2f(5400+pos_x,550)
    glVertex2f(5400+pos_x,600)
    glVertex2f(5550+pos_x,600)
    glVertex2f(5550+pos_x,550) 

    glVertex2f(5900+pos_x,650)
    glVertex2f(5900+pos_x,750)
    glVertex2f(5950+pos_x,750)
    glVertex2f(5950+pos_x,650) 

    glVertex2f(6400+pos_x,450)
    glVertex2f(6400+pos_x,550)
    glVertex2f(6700+pos_x,550)
    glVertex2f(6700+pos_x,450) 

    glVertex2f(6500+pos_x,550)
    glVertex2f(6500+pos_x,625)
    glVertex2f(6600+pos_x,625)
    glVertex2f(6600+pos_x,550)

    glVertex2f(6600+pos_x,400)
    glVertex2f(6600+pos_x,450)
    glVertex2f(6700+pos_x,450)
    glVertex2f(6700+pos_x,400) 

    glVertex2f(7150+pos_x,550)
    glVertex2f(7150+pos_x,600)
    glVertex2f(7250+pos_x,600)
    glVertex2f(7250+pos_x,550)

    glVertex2f(7550+pos_x,800)
    glVertex2f(7550+pos_x,850)
    glVertex2f(7600+pos_x,850)
    glVertex2f(7600+pos_x,800) 

    glVertex2f(7800+pos_x,700)
    glVertex2f(7800+pos_x,800)
    glVertex2f(7900+pos_x,800)
    glVertex2f(7900+pos_x,700) 

    glVertex2f(8600+pos_x,450)
    glVertex2f(8600+pos_x,500)
    glVertex2f(8900+pos_x,500)
    glVertex2f(8900+pos_x,450) 

    glVertex2f(8650+pos_x,500)
    glVertex2f(8650+pos_x,550)
    glVertex2f(8750+pos_x,550)
    glVertex2f(8750+pos_x,500) 

    glVertex2f(8800+pos_x,500)
    glVertex2f(8800+pos_x,550)
    glVertex2f(8850+pos_x,550)
    glVertex2f(8850+pos_x,500) 

    glVertex2f(8650+pos_x,400)
    glVertex2f(8650+pos_x,450)
    glVertex2f(8800+pos_x,450)
    glVertex2f(8800+pos_x,400) 

    glVertex2f(9100+pos_x,350)
    glVertex2f(9100+pos_x,400)
    glVertex2f(9150+pos_x,400)
    glVertex2f(9150+pos_x,350) 

    glVertex2f(9450+pos_x,450)
    glVertex2f(9450+pos_x,600)
    glVertex2f(9500+pos_x,600)
    glVertex2f(9500+pos_x,450) 

    glVertex2f(10100+pos_x,500)
    glVertex2f(10100+pos_x,550)
    glVertex2f(10350+pos_x,550)
    glVertex2f(10350+pos_x,500) 

    glVertex2f(10250+pos_x,550)
    glVertex2f(10250+pos_x,600)
    glVertex2f(10300+pos_x,600)
    glVertex2f(10300+pos_x,550) 

    glVertex2f(10150+pos_x,450)
    glVertex2f(10150+pos_x,500)
    glVertex2f(10250+pos_x,500)
    glVertex2f(10250+pos_x,450) 

    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0) 
    glEnd()

def coba() :
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(170,100+jump)
    glVertex2f(340,100+jump)
    glVertex2f(340,310+jump)
    glVertex2f(170,310+jump)
    glEnd()

def coba2():
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(2500 + pos_x,200)
    glVertex2f(2700 + pos_x,200)
    glVertex2f(2700 + pos_x,250)
    glVertex2f(2500 + pos_x,250)
    glEnd()

#Function even handling
def jumping(value) : #timer loncat keatas
    global jump, nabrak, right, left, pos_x
    if jump < 300  :
        if right == True :
            jump += 5
            pos_x -=5
        elif left == True :
            jump += 5
            pos_x +=5
        else :
            jump += 5
    else : 
        return fall_after_jump(0)
    glutTimerFunc(10,jumping,0)

def fall_after_jump(value) : #timer fall_to_canyon abis loncat
    global isJumping, jump, nabrak, right, left, pos_x
    if jump != 0  :
        if right == True :
            jump -= 5
            pos_x -=5
        elif left == True :
            jump -= 5
            pos_x +=5
    else : 
        isJumping = False
        return 
    glutTimerFunc(10,fall_after_jump,0)

def fall_to_canyon(value):
    global isJumping, jump, nabrak, right, left, pos_x, ulang
    if jump != -300 and nabrak is True :
        jump -=5
    else : 
        isJumping = False
        pos_x -= pos_x
        ulang = True
        return 
    glutTimerFunc(10,fall_to_canyon,0)

def keyboard(key,x,y):
    global jump, isJumping, pos_x, nabrak, obj_x1, obj_x2, right, left
    if key == GLUT_KEY_UP and isJumping is not True :
        isJumping = True
        jumping (0)
    elif key == GLUT_KEY_UP and isJumping is True :
        pass
    
    if key == GLUT_KEY_RIGHT :
        if pos_x <= -11010:
            pos_x -= 0
            isJumping = True
        else :
            canyon1_x1 = 990+pos_x
            canyon1_x2 = 1490+pos_x
            canyon2_x1 =2490+pos_x
            canyon2_x2 =2790+pos_x
            canyon3_x1 = 4490+pos_x
            canyon3_x2 = 4790+pos_x
            canyon4_x1 = 5990+pos_x
            canyon4_x2 = 6540+pos_x
            canyon5_x1 = 7449+pos_x
            canyon5_x2 = 7990+pos_x
            if (canyon1_x1 >= obj_x1 or canyon1_x2 <= obj_x2) and (canyon2_x1 >= obj_x1 or canyon2_x2 <= obj_x2) and (canyon3_x1 >= obj_x1 or canyon3_x2 <= obj_x2) and (canyon4_x1 >= obj_x1 or canyon4_x2 <= obj_x2) and (canyon5_x1 >= obj_x1 or canyon5_x2 <= obj_x2):
                isJumping = False
                pos_x -=10
                right = True
                left = False
            else :
                jump = 0
                nabrak = True
                pos_x -=0
                fall_to_canyon(0) 

    if key == GLUT_KEY_LEFT :
        if pos_x >= 0:
            pos_x += 0
            isJumping = True
        else :
            canyon1_x1 = 990+pos_x
            canyon1_x2 = 1490+pos_x
            canyon2_x1 = 2490+pos_x
            canyon2_x2 = 2790+pos_x
            canyon3_x1 = 4490+pos_x
            canyon3_x2 = 4790+pos_x
            canyon4_x1 = 5990+pos_x
            canyon4_x2 = 6540+pos_x
            canyon5_x1 = 7449+pos_x
            canyon5_x2 = 7990+pos_x
            if (canyon1_x1 >= obj_x1 or canyon1_x2 <= obj_x2) and (canyon2_x1 >= obj_x1 or canyon2_x2 <= obj_x2) and (canyon3_x1 >= obj_x1 or canyon3_x2 <= obj_x2) and (canyon4_x1 >= obj_x1 or canyon4_x2 <= obj_x2) and (canyon5_x1 >= obj_x1 or canyon5_x2 <= obj_x2):
                isJumping = False
                pos_x +=10
                right = False
                left = True
            else :
                jump = 0
                nabrak = True
                pos_x +=0
                fall_to_canyon(0)

#function menampilkan objek
jump = 0
isJumping = False
pos_x = 0
nabrak = False
right = False
left = False
ulang = False
obj_x1 = 170
obj_x2 = 350 


#function iterasi
def iterate():
    glViewport(0, 0,1920,1080)  #mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 2500, 0.0, 1400, 0.0, 1.0) #mengatur berapa blok yang digunakan
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#function menampilkan objek
def showScreen():
    glClearColor(0,255,255,0.5)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #membersihkan layar
    glLoadIdentity()
    iterate()
    tanah()
    Cerita_1()
    Cerita_2()
    Cerita_3()
    Cerita_4()
    Cerita_5()
    Cerita_6()
    canyon()
    TiangBendera()
    BenderaMerah()
    BenderaPutih()
    Awan()
    Awan2()
    Awan3()
    Awan4()
    karakter()
    glutSwapBuffers()
    

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920,1080) #mengatur ukuran window
glutInitWindowPosition(0, 0) #mengatur letak window
glutCreateWindow("CitraLoka : Explore The History") #memberi nama pada window
glutDisplayFunc(showScreen) 
glutIdleFunc(showScreen) 
glutSpecialFunc(keyboard)
glutMainLoop()
