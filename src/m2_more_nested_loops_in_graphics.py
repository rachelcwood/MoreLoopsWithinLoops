"""
This project demonstrates NESTED LOOPS (i.e., loops within loops)
in the context of TWO-DIMENSIONAL GRAPHICS.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and PUT_YOUR_NAME_HERE.
"""  # DONE 1

import rosegraphics as rg
import math


def main():
    """ Calls the other functions to test them. """
    run_test_draw_upside_down_wall()


def run_test_draw_upside_down_wall():
    """ Tests the    draw_upside_down_wall    function. """
    # Tests 1 and 2 are ALREADY DONE (here).
    window = rg.RoseWindow(550, 300, 'Upside-down wall, Tests 1 and 2')

    rectangle = rg.Rectangle(rg.Point(125, 230), rg.Point(155, 250))
    draw_upside_down_wall(rectangle, 8, window)

    rectangle = rg.Rectangle(rg.Point(375, 175), rg.Point(425, 225))
    draw_upside_down_wall(rectangle, 4, window)

    window.close_on_mouse_click()


def draw_upside_down_wall(rectangle, n, window):
    """
    See   MoreWalls.pdf   in this project for pictures that may
    help you better understand the following specification:

    Draws an "upside-down wall" on the given window, where:
      -- The BOTTOM of the wall is a single "brick"
            that is the given rg.Rectangle.
      -- There are n rows in the wall.
      -- Each row is a row of "bricks" that are the same size
            as the given rg.Rectangle.
      -- Each row has one more brick than the row below it.
      -- Each row is centered on the bottom row.

    Preconditions:
      :type rectangle: rg.Rectangle
      :type n: int
      :type window: rg.RoseWindow
    and n is nonnegative.
    """
    # ------------------------------------------------------------------
    # DONE 2. Implement and test this function.
    #     Some tests are already written for you (above).
    # ------------------------------------------------------------------
    rectorg = rectangle
    ulc = rectorg.get_upper_left_corner()
    lrc = rectorg.get_lower_right_corner()
    length = (ulc.x - lrc.x)
    height = ulc.y - lrc.y
    for k in range(n):
        for o in range(int(k/2)+1):
            rect = rg.Rectangle(rg.Point(ulc.x-((length/2)*(o*2+k%2)), ulc.y+(
                height*k)),
                                    rg.Point(
                         lrc.x-((length/2)*(o*2+k%2)), lrc.y+(height * k)))
            rect.outline_color='red'
            rect.attach_to(window)
            window.render()
            print(rect)
        for o in range(int(k/2)+1):
            rect = rg.Rectangle(rg.Point(ulc.x+((length/2)*(o*2+k%2)), ulc.y+(
                height*k)),
                                    rg.Point(
                         lrc.x+((length/2)*(o*2+k%2)), lrc.y+(height * k)))
            rect.outline_color='blue'
            rect.attach_to(window)
            window.render()
            print(rect)



# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
