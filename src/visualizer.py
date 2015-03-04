from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Visualizer():

	cell_size = 6 #px
	window = 0                                             
	width = 0
	height = 0
	data = [[]]
	world = False

	def __init__(self, **args):
		self.world = args['world']

		self.data = self.world.world
		self.width = self.world.width * self.cell_size
		self.height = self.world.height * self.cell_size
		glutInit()                                            
		glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
		glutInitWindowSize(self.width, self.height)              
		glutInitWindowPosition(0, 0)                           
		self.window = glutCreateWindow("Game of life - jkostrzewski")     
		glutDisplayFunc(self.draw)                               
		glutIdleFunc(self.draw)                           
		glutMainLoop() 


	def draw(self):
		self.world.next_generation()
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		glLoadIdentity()                                   
		self.refresh2d(self.width, self.height)                          
		glColor3f(0.7, 0.1, 0.1)                          
		self.draw_data()
		glutSwapBuffers() 

	def set_data(self, data):
		self.world = world

	def draw_data(self):
		
		for i in range(self.height/self.cell_size):
			for j in range(self.width/self.cell_size):
				if self.world.world[i][j].is_alive is True:
					self.draw_rect(j*self.cell_size, self.height-self.cell_size - i*self.cell_size, self.cell_size)                        

	def refresh2d(self, width, height):
	    glViewport(0, 0, width, height)
	    glMatrixMode(GL_PROJECTION)
	    glLoadIdentity()
	    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
	    glMatrixMode (GL_MODELVIEW)
	    glLoadIdentity()

	def draw_rect(self, x, y, size):
	    glBegin(GL_QUADS)                                  
	    glVertex2f(x, y)                                  
	    glVertex2f(x + size, y)                           
	    glVertex2f(x + size, y + size)                 
	    glVertex2f(x, y + size)                          
	    glEnd() 