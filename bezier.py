from graphics import *
import time

class bezier:
    def main(self):
        win = GraphWin('Bezier Curves', 500, 500)
        win.yUp()

        yaxis = Line(Point(0, -500), Point(0, 500))
        yaxis.move(250, 250)
        yaxis.draw(win)

        xaxis = Line(Point(-500, 0), Point(500, 0))
        xaxis.move(250, 250)
        xaxis.draw(win)

        x0=0
        y0=0

        x3=100
        y3=20

        x1=5
        y1=300

        x2=75
        y2=300

        xt=x0
        yt=y0

        t=0

        while t!=1 and xt<=x3:

            xt=pow((1-t),3)+(3*pow((1-t),2)*t*x1)+(3*pow((1-t),1)*t*t*x2)+t*t*t*x3
            yt = pow((1 - t), 3) + (3 * pow((1 - t), 2) * t * y1) + (3 * pow((1 - t), 1) * t * t * y2) + t * t * t * y3
            pt=Point(xt,yt)
            pt.move(250,250)
            pt.draw(win)

            pt = Point(xt, -yt)
            pt.move(250, 250)
            pt.draw(win)

            pt = Point(-xt, yt)
            pt.move(250, 250)
            pt.draw(win)

            pt = Point(-xt, -yt)
            pt.move(250, 250)
            pt.draw(win)



            t+=0.0005
        time.sleep(5)

x=bezier()
x.main()
