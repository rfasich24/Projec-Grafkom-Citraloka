#import library
from sys import flags, float_repr_style
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GLUT.freeglut import *

#------------------------------
def tanah():
    glBegin(GL_POLYGON) 
    glColor3ub(128,0,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,100)
    glVertex2f(11520+pos_x,100)
    glVertex2f(11520+pos_x,0)
    glEnd()

#Kotak yang berisi cerita
teks_1 = "Narasi Teks 1"
def Cerita_1(teks):
    glColor3f(0,0,0)
    glRasterPos( 700+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(600+pos_x,900)
    glVertex2f(600+pos_x,700)
    glVertex2f(1200+pos_x,700)
    glVertex2f(1200+pos_x,900)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

teks_2 = "Narasi Teks 2"
def Cerita_2(teks):
    glColor3f(0,0,0)
    glRasterPos( 2500+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(2400+pos_x,700)
    glVertex2f(2400+pos_x,900)
    glVertex2f(3000+pos_x,900)
    glVertex2f(3000+pos_x,700)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

teks_3 = "Narasi Teks 3"
def Cerita_3(teks):
    glColor3f(0,0,0)
    glRasterPos( 4500+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(4400+pos_x,700)
    glVertex2f(4400+pos_x,900)
    glVertex2f(5000+pos_x,900)
    glVertex2f(5000+pos_x,700)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

teks_4 = "Narasi Teks 4"
def Cerita_4(teks):
    glColor3f(0,0,0)
    glRasterPos( 6500+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(6400+pos_x,700)
    glVertex2f(6400+pos_x,900)
    glVertex2f(7000+pos_x,900)
    glVertex2f(7000+pos_x,700)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

teks_5 = "Narasi Teks 5"
def Cerita_5(teks):
    glColor3f(0,0,0)
    glRasterPos( 8500+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(8400+pos_x,700)
    glVertex2f(8400+pos_x,900)
    glVertex2f(9000+pos_x,900)
    glVertex2f(9000+pos_x,700)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

teks_6 = "Narasi Teks 6"
def Cerita_6(teks):
    glColor3f(0,0,0)
    glRasterPos( 10300+pos_x,800)
    glColor3ub(255, 215,0)
    glBegin(GL_POLYGON)
    glVertex2f(10200+pos_x,700)
    glVertex2f(10200+pos_x,900)
    glVertex2f(10800+pos_x,900)
    glVertex2f(10800+pos_x,700)
    glEnd()
    for i in teks:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(i))

#LAYER 1
def RumahBagianBawah():
    glBegin(GL_QUADS)
    glColor3ub(255,255,153)
    glVertex2f(100+pos_x,100)
    glVertex2f(200+pos_x,200)
    glVertex2f(400+pos_x,200)
    glVertex2f(500+pos_x,100)
    glEnd()

def RumahBagianTengah():
    glBegin(GL_QUADS)
    glColor3ub(255,255,153)
    glVertex2f(200+pos_x,200)
    glVertex2f(200+pos_x,400)
    glVertex2f(400+pos_x,400)
    glVertex2f(400+pos_x,200)
    glEnd()
    
def Atap():
    glBegin(GL_TRIANGLES)
    glColor3ub(152,76,0)
    glVertex2f(100+pos_x,400)
    glVertex2f(300+pos_x,500)
    glVertex2f(500+pos_x,400)
    glEnd()

def PintuRumahKiri():
    glBegin(GL_QUADS)
    glColor3ub(153,76,0)
    glVertex2f(250+pos_x,100)
    glVertex2f(250+pos_x,175)
    glVertex2f(300+pos_x,175)
    glVertex2f(300+pos_x,100)
    glEnd()

def PintuRumahKanan():
    glBegin(GL_QUADS)
    glColor3ub(153,76,0)
    glVertex2f(300+pos_x,100)
    glVertex2f(300+pos_x,175)
    glVertex2f(350+pos_x,175)
    glVertex2f(350+pos_x,100)
    glEnd()

#Detil Garis Layer 1
def D_RumahBagianBawah():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(100+pos_x,100)
    glVertex2f(200+pos_x,200)
    glVertex2f(400+pos_x,200)
    glVertex2f(500+pos_x,100)
    glEnd()

def D_RumahBagianTengah():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(200+pos_x,200)
    glVertex2f(200+pos_x,400)
    glVertex2f(400+pos_x,400)
    glVertex2f(400+pos_x,200)
    glEnd()
    
def D_Atap():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(100+pos_x,400)
    glVertex2f(300+pos_x,500)
    glVertex2f(500+pos_x,400)
    glEnd()

def D_PintuRumahKiri():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(250+pos_x,100)
    glVertex2f(250+pos_x,175)
    glVertex2f(300+pos_x,175)
    glVertex2f(300+pos_x,100)
    glEnd()

def D_PintuRumahKanan():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(300+pos_x,100)
    glVertex2f(300+pos_x,175)
    glVertex2f(350+pos_x,175)
    glVertex2f(350+pos_x,100)
    glEnd()

#LAYER 2
def Objek2_1():
    glBegin(GL_QUADS)
    glColor3ub(255, 204,153)
    glVertex2f(2000+pos_x,100)
    glVertex2f(2200+pos_x,200)
    glVertex2f(2400+pos_x,200)
    glVertex2f(2400+pos_x,100)
    glEnd()

def Objek2_2():
    glBegin(GL_QUADS)
    glColor3ub(255, 0,0)
    glVertex2f(2500+pos_x,200)
    glVertex2f(2500+pos_x,250)
    glVertex2f(2700+pos_x,250)
    glVertex2f(2700+pos_x,200)
    glEnd()

def Objek2_3():
    glBegin(GL_QUADS)
    glColor3ub(255, 255,255)
    glVertex2f(2800+pos_x,250)
    glVertex2f(2800+pos_x,300)
    glVertex2f(3000+pos_x,300)
    glVertex2f(3000+pos_x,250)
    glEnd()

def Objek2_4():
    glBegin(GL_QUADS)
    glColor3ub(255, 0,0)
    glVertex2f(3100+pos_x,300)
    glVertex2f(3100+pos_x,350)
    glVertex2f(3300+pos_x,350)
    glVertex2f(3300+pos_x,300)
    glEnd()

def Objek2_5():
    glBegin(GL_QUADS)
    glColor3ub(255, 255,255)
    glVertex2f(3400+pos_x,350)
    glVertex2f(3400+pos_x,400)
    glVertex2f(3600+pos_x,400)
    glVertex2f(3600+pos_x,350)
    glEnd()

def Objek2_6():
    glBegin(GL_QUADS)
    glColor3ub(255, 204,153)
    glVertex2f(3700+pos_x,100)
    glVertex2f(3700+pos_x,500)
    glVertex2f(3800+pos_x,500)
    glVertex2f(3800+pos_x,100)
    glEnd()
#Detail Layer 2
def D_Objek2_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2000+pos_x,100)
    glVertex2f(2200+pos_x,200)
    glVertex2f(2400+pos_x,200)
    glVertex2f(2400+pos_x,100)
    glEnd()

def D_Objek2_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2500+pos_x,200)
    glVertex2f(2500+pos_x,250)
    glVertex2f(2700+pos_x,250)
    glVertex2f(2700+pos_x,200)
    glEnd()

def D_Objek2_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2800+pos_x,250)
    glVertex2f(2800+pos_x,300)
    glVertex2f(3000+pos_x,300)
    glVertex2f(3000+pos_x,250)
    glEnd()

def D_Objek2_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3100+pos_x,300)
    glVertex2f(3100+pos_x,350)
    glVertex2f(3300+pos_x,350)
    glVertex2f(3300+pos_x,300)
    glEnd()

def D_Objek2_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3400+pos_x,350)
    glVertex2f(3400+pos_x,400)
    glVertex2f(3600+pos_x,400)
    glVertex2f(3600+pos_x,350)
    glEnd()

def D_Objek2_6():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3700+pos_x,100)
    glVertex2f(3700+pos_x,500)
    glVertex2f(3800+pos_x,500)
    glVertex2f(3800+pos_x,100)
    glEnd()

#LAYER 3
def Objek3_1():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4000+pos_x,250)
    glVertex2f(4200+pos_x,250)
    glVertex2f(4100+pos_x,150)
    glEnd()

def Objek3_2():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4400+pos_x,350)
    glVertex2f(4600+pos_x,350)
    glVertex2f(4500+pos_x,270)
    glEnd()

def Objek3_3():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4800+pos_x,250)
    glVertex2f(5000+pos_x,250)
    glVertex2f(4900+pos_x,150)
    glEnd()

def Objek3_4():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(5200+pos_x,350)
    glVertex2f(5400+pos_x,350)
    glVertex2f(5300+pos_x,250)
    glEnd()

def Objek3_5():
    glBegin(GL_QUADS)
    glColor3ub(0, 225,0)
    glVertex2f(5600+pos_x,100)
    glVertex2f(5600+pos_x,500)
    glVertex2f(5750+pos_x,500)
    glVertex2f(5750+pos_x,100)
    glEnd()
#Detil Layer 3
def D_Objek3_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4000+pos_x,250)
    glVertex2f(4200+pos_x,250)
    glVertex2f(4100+pos_x,150)
    glEnd()

def D_Objek3_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4400+pos_x,350)
    glVertex2f(4600+pos_x,350)
    glVertex2f(4500+pos_x,270)
    glEnd()

def D_Objek3_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4800+pos_x,250)
    glVertex2f(5000+pos_x,250)
    glVertex2f(4900+pos_x,150)
    glEnd()

def D_Objek3_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5200+pos_x,350)
    glVertex2f(5400+pos_x,350)
    glVertex2f(5300+pos_x,250)
    glEnd()

def D_Objek3_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5600+pos_x,100)
    glVertex2f(5600+pos_x,500)
    glVertex2f(5750+pos_x,500)
    glVertex2f(5750+pos_x,100)
    glEnd()

#LAYER 4
def Objek4_1():
    glBegin(GL_QUADS)
    glColor3ub(255, 102,102)
    glVertex2f(5900+pos_x,300)
    glVertex2f(7500+pos_x,300)
    glVertex2f(7000+pos_x,100)
    glVertex2f(6400+pos_x,100)
    glEnd()

def Objek4_2():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(6200+pos_x,300)
    glVertex2f(6200+pos_x,450)
    glVertex2f(6400+pos_x,450)
    glVertex2f(6400+pos_x,300)
    glEnd()

def Objek4_3():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(6600+pos_x,300)
    glVertex2f(6600+pos_x,350)
    glVertex2f(7000+pos_x,350)
    glVertex2f(7000+pos_x,300)
    glEnd()

def Objek4_4():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(7100+pos_x,300)
    glVertex2f(7100+pos_x,500)
    glVertex2f(7250+pos_x,500)
    glVertex2f(7250+pos_x,300)
    glEnd()

def Objek4_5():
    glBegin(GL_TRIANGLES)
    glColor3ub(152,76,0)
    glVertex2f(7250+pos_x,500)
    glVertex2f(7500+pos_x,300)
    glVertex2f(7250+pos_x,300)
    glEnd()

#Detil Layer 4
def D_Objek4_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5900+pos_x,300)
    glVertex2f(7500+pos_x,300)
    glVertex2f(7000+pos_x,100)
    glVertex2f(6400+pos_x,100)
    glEnd()

def D_Objek4_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(6200+pos_x,300)
    glVertex2f(6200+pos_x,450)
    glVertex2f(6400+pos_x,450)
    glVertex2f(6400+pos_x,300)
    glEnd()

def D_Objek4_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(6600+pos_x,300)
    glVertex2f(6600+pos_x,350)
    glVertex2f(7000+pos_x,350)
    glVertex2f(7000+pos_x,300)
    glEnd()

def D_Objek4_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(7100+pos_x,300)
    glVertex2f(7100+pos_x,500)
    glVertex2f(7250+pos_x,500)
    glVertex2f(7250+pos_x,300)
    glEnd()

def D_Objek4_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(7250+pos_x,500)
    glVertex2f(7500+pos_x,300)
    glVertex2f(7250+pos_x,300)
    glEnd()

#LAYER 5
def Objek5_1():
    glBegin(GL_QUADS)
    glColor3ub(192,192,192)
    glVertex2f(8000+pos_x,300)
    glVertex2f(8300+pos_x,500)
    glVertex2f(8600+pos_x,500)
    glVertex2f(8600+pos_x,300)
    glEnd()

def Objek5_2():
    glBegin(GL_QUADS)
    glColor3ub(192,192,192)
    glVertex2f(8800+pos_x,100)
    glVertex2f(8800+pos_x,500)
    glVertex2f(9200+pos_x,500)
    glVertex2f(9500+pos_x,100)
    glEnd()

#Detil layer 5
def D_Objek5_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(8000+pos_x,300)
    glVertex2f(8300+pos_x,500)
    glVertex2f(8600+pos_x,500)
    glVertex2f(8600+pos_x,300)
    glEnd()

def D_Objek5_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(8800+pos_x,100)
    glVertex2f(8800+pos_x,500)
    glVertex2f(9200+pos_x,500)
    glVertex2f(9500+pos_x,100)
    glEnd()

#LAYER 6
def Objek6_1():
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(11350+pos_x,100)
    glVertex2f(11350+pos_x,800)
    glVertex2f(11400+pos_x,800)
    glVertex2f(11400+pos_x,100)
    glEnd()

#Detil layer 6
def D_Objek6_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(11350+pos_x,100)
    glVertex2f(11350+pos_x,800)
    glVertex2f(11400+pos_x,800)
    glVertex2f(11400+pos_x,100)
    glEnd()

def rintanganX():
    glBegin(GL_QUADS)
    glColor3ub(102, 225,102)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0)
    glVertex2f(0+pos_x,0)
    glEnd()


#------------------------------
def karakter():
    # glScaled(2,2,0)
    glTranslated(100,80+jump_height,0)
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

#Function even handling
def jump_timer(value) : #timer loncat keatas
    global jump_height
    if jump_height < 300  :
        jump_height += 5
    else : 
        return down_timer(0)
    glutTimerFunc(10,jump_timer,0)

def down_timer(value) : #timer jatuh abis loncat
    global isJumping
    global jump_height
    if jump_height != 0  :
        jump_height -= 5
    else : 
        isJumping = False
        return 
    glutTimerFunc(10,down_timer,0)

def jump_button(key,x,y) : #Fungsi Input Keyboard loncat
    global isJumping,isPlaying  
    global pos_x
 
    if key == GLUT_KEY_UP and isJumping is not True :
        isJumping = True
        jump_timer(0)
        print("loncat")

    elif key == GLUT_KEY_UP and isJumping is True :
        pass
    
    # Untuk mengubah posisi kotak
    if key == GLUT_KEY_RIGHT :
        pos_x -= 15
        print("Tombol Kanan ditekan ", "x : ", pos_x)
    elif key == GLUT_KEY_LEFT :
        pos_x += 15
        print("Tombol Kanan ditekan ", "x : ", pos_x)

isJumping = False
jump_height = 0
isPlaying = True
pos_x = 0


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
    Cerita_1(teks_1)
    Cerita_2(teks_2)
    Cerita_3(teks_3)
    Cerita_4(teks_4)
    Cerita_5(teks_5)
    Cerita_6(teks_6)
    RumahBagianBawah()
    RumahBagianTengah()
    Atap()
    PintuRumahKanan()
    PintuRumahKiri()
    D_RumahBagianBawah()
    D_RumahBagianTengah()
    D_Atap()
    D_PintuRumahKanan()
    D_PintuRumahKiri()
    Objek2_1()
    Objek2_2()
    Objek2_3()
    Objek2_4()
    Objek2_5()
    Objek2_6()
    D_Objek2_1()
    D_Objek2_2()
    D_Objek2_3()
    D_Objek2_4()
    D_Objek2_5()
    D_Objek2_6()
    Objek3_1()
    Objek3_2()
    Objek3_3()
    Objek3_4()
    Objek3_5()
    D_Objek3_1()
    D_Objek3_2()
    D_Objek3_3()
    D_Objek3_4()
    D_Objek3_5()
    Objek4_1()
    Objek4_2()
    Objek4_3()
    Objek4_4()
    Objek4_5()
    D_Objek4_1()
    D_Objek4_2()
    D_Objek4_3()
    D_Objek4_4()
    D_Objek4_5()
    Objek5_1()
    Objek5_2()
    D_Objek5_1()
    D_Objek5_2()
    Objek6_1()
    D_Objek6_1
    karakter()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920,1080) #engatur ukuran window
glutInitWindowPosition(0, 0) #mengatur letak window
wind = glutCreateWindow("CitraLoka") #memberi nama pada window
glutDisplayFunc(showScreen) 
glutIdleFunc(showScreen) 
glutSpecialFunc(jump_button)
glutMainLoop() #memulai keseluruhan program
