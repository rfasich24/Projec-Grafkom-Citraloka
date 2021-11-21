#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
w,h= 900,1000

#tanah atau alas dari Game
def tanah():
    glBegin(GL_POLYGON) 
    glColor3ub(128,0,0)
    glVertex2f(0,0)
    glVertex2f(0,100)
    glVertex2f(11520,100)
    glVertex2f(11520,0)
    glEnd()

#Kotak yang berisi cerita
def kotak1():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(600,900)
    glVertex2f(600,700)
    glVertex2f(1200,700)
    glVertex2f(1200,900)
    glEnd()

def kotak2():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(2400,700)
    glVertex2f(2400,900)
    glVertex2f(3000,900)
    glVertex2f(3000,700)
    glEnd()

def kotak3():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(4400,700)
    glVertex2f(4400,900)
    glVertex2f(5000,900)
    glVertex2f(5000,700)
    glEnd()

def kotak4():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(6400,700)
    glVertex2f(6400,900)
    glVertex2f(7000,900)
    glVertex2f(7000,700)
    glEnd()

def kotak5():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(8400,700)
    glVertex2f(8400,900)
    glVertex2f(9000,900)
    glVertex2f(9000,700)
    glEnd()

def kotak6():
    glBegin(GL_POLYGON) 
    glColor3ub(255, 215,0)
    glVertex2f(10200,700)
    glVertex2f(10200,900)
    glVertex2f(10800,900)
    glVertex2f(10800,700)
    glEnd()

#LAYER 1
def RumahBagianBawah():
    glBegin(GL_QUADS)
    glColor3ub(255,255,153)
    glVertex2f(100,100)
    glVertex2f(200,200)
    glVertex2f(400,200)
    glVertex2f(500,100)
    glEnd()

def RumahBagianTengah():
    glBegin(GL_QUADS)
    glColor3ub(255,255,153)
    glVertex2f(200,200)
    glVertex2f(200,400)
    glVertex2f(400,400)
    glVertex2f(400,200)
    glEnd()
    
def Atap():
    glBegin(GL_TRIANGLES)
    glColor3ub(152,76,0)
    glVertex2f(100,400)
    glVertex2f(300,500)
    glVertex2f(500,400)
    glEnd()

def PintuRumahKiri():
    glBegin(GL_QUADS)
    glColor3ub(153,76,0)
    glVertex2f(250,100)
    glVertex2f(250,175)
    glVertex2f(300,175)
    glVertex2f(300,100)
    glEnd()

def PintuRumahKanan():
    glBegin(GL_QUADS)
    glColor3ub(153,76,0)
    glVertex2f(300,100)
    glVertex2f(300,175)
    glVertex2f(350,175)
    glVertex2f(350,100)
    glEnd()

#Detil Garis Layer 1
def D_RumahBagianBawah():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(100,100)
    glVertex2f(200,200)
    glVertex2f(400,200)
    glVertex2f(500,100)
    glEnd()

def D_RumahBagianTengah():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(200,200)
    glVertex2f(200,400)
    glVertex2f(400,400)
    glVertex2f(400,200)
    glEnd()
    
def D_Atap():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(100,400)
    glVertex2f(300,500)
    glVertex2f(500,400)
    glEnd()

def D_PintuRumahKiri():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(250,100)
    glVertex2f(250,175)
    glVertex2f(300,175)
    glVertex2f(300,100)
    glEnd()

def D_PintuRumahKanan():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(300,100)
    glVertex2f(300,175)
    glVertex2f(350,175)
    glVertex2f(350,100)
    glEnd()

#LAYER 2
def Objek2_1():
    glBegin(GL_QUADS)
    glColor3ub(255, 204,153)
    glVertex2f(2000,100)
    glVertex2f(2200,200)
    glVertex2f(2400,200)
    glVertex2f(2400,100)
    glEnd()

def Objek2_2():
    glBegin(GL_QUADS)
    glColor3ub(255, 0,0)
    glVertex2f(2500,200)
    glVertex2f(2500,250)
    glVertex2f(2700,250)
    glVertex2f(2700,200)
    glEnd()

def Objek2_3():
    glBegin(GL_QUADS)
    glColor3ub(255, 255,255)
    glVertex2f(2800,250)
    glVertex2f(2800,300)
    glVertex2f(3000,300)
    glVertex2f(3000,250)
    glEnd()

def Objek2_4():
    glBegin(GL_QUADS)
    glColor3ub(255, 0,0)
    glVertex2f(3100,300)
    glVertex2f(3100,350)
    glVertex2f(3300,350)
    glVertex2f(3300,300)
    glEnd()

def Objek2_5():
    glBegin(GL_QUADS)
    glColor3ub(255, 255,255)
    glVertex2f(3400,350)
    glVertex2f(3400,400)
    glVertex2f(3600,400)
    glVertex2f(3600,350)
    glEnd()

def Objek2_6():
    glBegin(GL_QUADS)
    glColor3ub(255, 204,153)
    glVertex2f(3700,100)
    glVertex2f(3700,500)
    glVertex2f(3800,500)
    glVertex2f(3800,100)
    glEnd()
#Detail Layer 2
def D_Objek2_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2000,100)
    glVertex2f(2200,200)
    glVertex2f(2400,200)
    glVertex2f(2400,100)
    glEnd()

def D_Objek2_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2500,200)
    glVertex2f(2500,250)
    glVertex2f(2700,250)
    glVertex2f(2700,200)
    glEnd()

def D_Objek2_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(2800,250)
    glVertex2f(2800,300)
    glVertex2f(3000,300)
    glVertex2f(3000,250)
    glEnd()

def D_Objek2_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3100,300)
    glVertex2f(3100,350)
    glVertex2f(3300,350)
    glVertex2f(3300,300)
    glEnd()

def D_Objek2_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3400,350)
    glVertex2f(3400,400)
    glVertex2f(3600,400)
    glVertex2f(3600,350)
    glEnd()

def D_Objek2_6():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(3700,100)
    glVertex2f(3700,500)
    glVertex2f(3800,500)
    glVertex2f(3800,100)
    glEnd()

#LAYER 3
def Objek3_1():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4000,250)
    glVertex2f(4200,250)
    glVertex2f(4100,150)
    glEnd()

def Objek3_2():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4400,350)
    glVertex2f(4600,350)
    glVertex2f(4500,270)
    glEnd()

def Objek3_3():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(4800,250)
    glVertex2f(5000,250)
    glVertex2f(4900,150)
    glEnd()

def Objek3_4():
    glBegin(GL_TRIANGLES)
    glColor3ub(0, 225,0)
    glVertex2f(5200,350)
    glVertex2f(5400,350)
    glVertex2f(5300,250)
    glEnd()

def Objek3_5():
    glBegin(GL_QUADS)
    glColor3ub(0, 225,0)
    glVertex2f(5600,100)
    glVertex2f(5600,500)
    glVertex2f(5750,500)
    glVertex2f(5750,100)
    glEnd()
#Detil Layer 3
def D_Objek3_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4000,250)
    glVertex2f(4200,250)
    glVertex2f(4100,150)
    glEnd()

def D_Objek3_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4400,350)
    glVertex2f(4600,350)
    glVertex2f(4500,270)
    glEnd()

def D_Objek3_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(4800,250)
    glVertex2f(5000,250)
    glVertex2f(4900,150)
    glEnd()

def D_Objek3_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5200,350)
    glVertex2f(5400,350)
    glVertex2f(5300,250)
    glEnd()

def D_Objek3_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5600,100)
    glVertex2f(5600,500)
    glVertex2f(5750,500)
    glVertex2f(5750,100)
    glEnd()

#LAYER 4
def Objek4_1():
    glBegin(GL_QUADS)
    glColor3ub(255, 102,102)
    glVertex2f(5900,300)
    glVertex2f(7500,300)
    glVertex2f(7000,100)
    glVertex2f(6400,100)
    glEnd()

def Objek4_2():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(6200,300)
    glVertex2f(6200,450)
    glVertex2f(6400,450)
    glVertex2f(6400,300)
    glEnd()

def Objek4_3():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(6600,300)
    glVertex2f(6600,350)
    glVertex2f(7000,350)
    glVertex2f(7000,300)
    glEnd()

def Objek4_4():
    glBegin(GL_QUADS)
    glColor3ub(152,76,0)
    glVertex2f(7100,300)
    glVertex2f(7100,500)
    glVertex2f(7250,500)
    glVertex2f(7250,300)
    glEnd()

def Objek4_5():
    glBegin(GL_TRIANGLES)
    glColor3ub(152,76,0)
    glVertex2f(7250,500)
    glVertex2f(7500,300)
    glVertex2f(7250,300)
    glEnd()

#Detil Layer 4
def D_Objek4_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(5900,300)
    glVertex2f(7500,300)
    glVertex2f(7000,100)
    glVertex2f(6400,100)
    glEnd()

def D_Objek4_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(6200,300)
    glVertex2f(6200,450)
    glVertex2f(6400,450)
    glVertex2f(6400,300)
    glEnd()

def D_Objek4_3():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(6600,300)
    glVertex2f(6600,350)
    glVertex2f(7000,350)
    glVertex2f(7000,300)
    glEnd()

def D_Objek4_4():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(7100,300)
    glVertex2f(7100,500)
    glVertex2f(7250,500)
    glVertex2f(7250,300)
    glEnd()

def D_Objek4_5():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(7250,500)
    glVertex2f(7500,300)
    glVertex2f(7250,300)
    glEnd()

#LAYER 5
def Objek5_1():
    glBegin(GL_QUADS)
    glColor3ub(192,192,192)
    glVertex2f(8000,300)
    glVertex2f(8300,500)
    glVertex2f(8600,500)
    glVertex2f(8600,300)
    glEnd()

def Objek5_2():
    glBegin(GL_QUADS)
    glColor3ub(192,192,192)
    glVertex2f(8800,100)
    glVertex2f(8800,500)
    glVertex2f(9200,500)
    glVertex2f(9500,100)
    glEnd()

#Detil layer 5
def D_Objek5_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(8000,300)
    glVertex2f(8300,500)
    glVertex2f(8600,500)
    glVertex2f(8600,300)
    glEnd()

def D_Objek5_2():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(8800,100)
    glVertex2f(8800,500)
    glVertex2f(9200,500)
    glVertex2f(9500,100)
    glEnd()

#LAYER 6
def Objek6_1():
    glBegin(GL_QUADS)
    glColor3ub(255,255,255)
    glVertex2f(11350,100)
    glVertex2f(11350,800)
    glVertex2f(11400,800)
    glVertex2f(11400,100)
    glEnd()

#Detil layer 6
def D_Objek6_1():
    glBegin(GL_LINE_LOOP)
    glColor3ub(0,0,0)
    glVertex2f(11350,100)
    glVertex2f(11350,800)
    glVertex2f(11400,800)
    glVertex2f(11400,100)
    glEnd()

def rintanganX():
    glBegin(GL_QUADS)
    glColor3ub(102, 225,102)
    glVertex2f(0,0)
    glVertex2f(0,0)
    glVertex2f(0,0)
    glVertex2f(0,0)
    glEnd()
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
    kotak1()
    kotak2()
    kotak3()
    kotak4()
    kotak5()
    kotak6()
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
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920,1080) #engatur ukuran window
glutInitWindowPosition(0, 0) #mengatur letak window
wind = glutCreateWindow("GLUT Program") #memberi nama pada window
glutDisplayFunc(showScreen) 
glutIdleFunc(showScreen) 
glutMainLoop() #memulai keseluruhan program
