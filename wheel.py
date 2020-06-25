from graphics import *
from math import sin, cos, atan2, pi, radians


def main():
    win = GraphWin("Wheel of the Worst!", 700, 700)

    pt = Point(win.getHeight() / 2, win.getWidth() / 2)

    radius = win.getWidth() / 3
    cir = Circle(pt, radius)
    cir.draw(win)
    angle = radians(0)
    line = Line(pt, Point(pt.getX() + radius * cos(angle), pt.getY() + radius * sin(-angle)))
    line.draw(win)

main()
