"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Yi Li.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

lily = rg.SimpleTurtle()
lily.pen = rg.Pen('red', 2)
lily.speed = 20

size = 100

for k in range(10):
    lily.draw_square(size)

    lily.pen_up()
    lily.right(45)
    lily.forward(20)
    lily.left(45)

    lily.pen_down()
    size = size-10

parker = rg.SimpleTurtle('turtle')
parker.pen = rg.Pen('blue', 2)
parker.speed = 20

size2 = 100

for g in range(10):
    parker.draw_square(size2)

    parker.pen_up()
    parker.left(90)
    parker.forward(20)
    parker.left(90)

    parker.pen_down()
    size2 = size2-10

window.close_on_mouse_click()
