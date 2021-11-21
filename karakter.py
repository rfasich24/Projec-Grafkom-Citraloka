#import library
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def karakter():
    glScaled(2,2,0)
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

#function iterasi
def iterate():
    glViewport(0, 0, 1920,1080)  #mengatur area pandang
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 1920, 0.0, 1080, 0.0, 1.0) #mengatur berapa blok yang digunakan
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

#function menampilkan objek
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #membersihkan layar
    glLoadIdentity()
    iterate()
    karakter()
    glutSwapBuffers() #utk membersihkan layar, double buffering

glutInit() #inisialisasi glut
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1920,1080) #engatur ukuran window
glutInitWindowPosition(0, 0) #mengatur letak window
wind = glutCreateWindow("GLUT Program Ironman") #memberi nama pada window
glutDisplayFunc(showScreen) 
glutIdleFunc(showScreen) 
glutMainLoop() #memulai keseluruhan program
