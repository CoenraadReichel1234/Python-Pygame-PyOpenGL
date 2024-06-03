import pygame as pg
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import Cube
import Pyramid
import Prism

class Display:
    def __init__(self):
        self.object_files = [Cube, Pyramid, Prism]
        self.current_object = 0
        self.display = (800, 600)
        pg.init()
        pg.display.set_mode(self.display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (self.display[0]/self.display[1]), 0.1, 50.0)
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)  
        glTranslatef(0, 0, -5)
        glRotatef(25, 2, 10, 0)

    def load_objects(self, object_module):
        return object_module.verticies, object_module.edges, object_module.surfaces, object_module.colors

    def renderObject(self, verticies, edges, surfaces, colors):
        glBegin(GL_QUADS)
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x += 1
                glColor3fv(colors[x])
                glVertex3fv(verticies[vertex])
        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()

    def run(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                self.handle_keys(event)
            
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            verticies, edges, surfaces, colors = self.load_objects(self.object_files[self.current_object])
            self.renderObject(verticies, edges, surfaces, colors)
            pg.display.flip()
            pg.time.wait(10)

    def handle_keys(self, event):
        # Handle key presses for navigation and object manipulation
        if event.type == pg.KEYDOWN:
            # Move to next object
            if event.key == pg.K_SPACE:
                self.current_object = (self.current_object + 1) % len(self.object_files)
            # Translate object
            # X-axis
            elif event.key == pg.K_RIGHT:
                glTranslatef(0.5, 0, 0)
            elif event.key == pg.K_LEFT:
                glTranslatef(-0.5, 0, 0)
            # Y-axis
            elif event.key == pg.K_UP:
                glTranslatef(0, 0.5, 0)
            elif event.key == pg.K_DOWN:
                glTranslatef(0, -0.5, 0)
            # Z-axis
            elif event.key == pg.K_TAB:
                glTranslatef(0, 0, 0.5)
            elif event.key == pg.K_MINUS:
                glTranslatef(0, 0, -0.5)
            # Rotate object
            # X-axis
            elif event.key == pg.K_w:
                glRotatef(25, 0.5, 0, 0)
            elif event.key == pg.K_s:
                glRotatef(25, -0.5, 0, 0)
            # Y-axis
            elif event.key == pg.K_e:
                glRotatef(25, 0, 0.5, 0)
            elif event.key == pg.K_d:
                glRotatef(25, 0, -0.5, 0)
            # Z-axis
            elif event.key == pg.K_r:
                glRotatef(25, 0, 0, 0.5)
            elif event.key == pg.K_f:
                glRotatef(25, 0, 0, -0.5)
            # Scaling object
            # Grow
            elif event.key == pg.K_y:
                glScalef(1.5, 1.5, 1.5)
            # Shrink
            elif event.key == pg.K_h:
                glScalef(0.5, 0.5, 0.5)

# To run the display
if __name__ == "__main__":
    display = Display()
    display.run()
