# Python-Pygame-PyOpenGL
Assignment Repo

1. Make sure that all necessary libraries are imported in the Display.py file, as well as the Cube.py, Pyramid.py and Prism.py files.
    pygame
    OpengGL.GL
    OpenGL.GLU

2. The objects will be displayed within a while loop, and will only stop once the pygame window is closed.

3. User interaction controls/instructions
    Navigation:
        Pressing the Spacebar cycles through different objects.

        Arrow keys translate the object along the X, Y, and Z axes.(Arrow Up translates Y-axis in the positive direction, Arrow Down translates the Y-axis in the negative direction, Arrow Left the X-axis in the negative direction and Arrow Right the X-axis in the positive direction)

        Tab and Minus keys translate along the Z-axis. (Make sure to press the Minus key on the top of the keyboard if there are two minus keys present, Tab key translates the Z-axis in the positive direction while Minus key translates the Z-axis in the negative direction)

    Rotation:
        W(Positive direction) and S(Negative direction) keys rotate the object around the X-axis.
        E(Positive direction) and D(Negative direction) keys rotate around the Y-axis.
        R(Positive direction) and F(Negative direction) keys rotate around the Z-axis.
    Scaling:
        Y scales the object up.
        H scales it down.
