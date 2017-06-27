from graphics import *
import time

def Flood_Fill():
    win = GraphWin('MidPoint Circle Algorithm', 500, 500)
    win.yUp()

    pt = Point(250, 250)
    pt.draw(win)
    r=240


    cir = Circle(pt, r)
    cir.setOutline('red')
    #cir.move(250,250)
    cir.draw(win)
    time.sleep(2)
    return cir, r, win

def set_old_color():
    cir, r, win=Flood_Fill()

    x,y=250,250

    if(x*x+y*y-r*r!=0):
        Point(x,y).draw(win)

    if ((x+1) * (x+1) + y * y - r * r != 0):
        Point(x+1, y).draw(win)
        x=x+1
    if (x * x + y * y - r * r != 0):
        Point(x, y).draw(win)

    if (x * x + y * y - r * r != 0):
        Point(x, y).draw(win)





def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    #pt.draw(win)
    pt.move(250,250) #shifting 0,0 to the right by dx=250, dy=250
    pt.draw(win)



def main():
    Flood_Fill()

if __name__ == "__main__":
    main()
