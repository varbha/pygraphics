from graphics import *

import time


def main():
    #make a polygon
    win = GraphWin('Shearing and Reflection', 500, 500)
    win.yUp()

    yaxis=Line(Point(0,-500),Point(0,500))
    yaxis.move(250,250)
    yaxis.draw(win)

    xaxis=Line(Point(-500,0),Point(500,0))
    xaxis.move(250,250)
    xaxis.draw(win)



    aPolygon = Polygon([Point(0, 0), Point(50, 100), Point(100, 0)])
    aPolygon.move(250,250)

    aPolygon.draw(win)



    aPolygon2 = Polygon([Point(0, 0), Point(85,170), Point(100, 0)])
    aPolygon2.move(250, 250)
    aPolygon2.setOutline("yellow")

    aPolygon2.draw(win)

    areflection=Polygon([Point(0,0), Point(-50,100),Point(-100,0)])
    areflection.move(250,250)
    areflection.setOutline("red")
    areflection.draw(win)

    areflection2 = Polygon([Point(0, 0), Point(50, -100), Point(100, 0)])
    areflection2.move(250, 250)
    areflection2.setOutline("blue")
    areflection2.draw(win)

    areflection = Polygon([Point(0, 0), Point(-50, -100), Point(-100, 0)])
    areflection.move(250, 250)
    areflection.setOutline("green")
    areflection.draw(win)

    time.sleep(60)
    win.close()


if __name__ == '__main__':
    main()

