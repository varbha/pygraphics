from graphics import *
import time

win = GraphWin('MidPoint Circle Algorithm', 1000, 1000)
win.yUp()



def ellipse(xc,yc,a,b):

    a2 = a * a
    b2 = b * b
    twoa2 = 2 * a2
    twob2 = 2 * b2
    p=0
    x = 0
    y = b
    px = 0
    py = twoa2 * y

    # /* Plot the initial point in each quadrant. */
    ellipsePlotPoints(xc, yc, x, y)

    p = round(b2 - (a2 * b) + (0.25 * a2))
    while (px < py): #since the condition for moving over to r2 is 2b^2x>=2a^2y
        x += 1
        px = twob2*x
        if (p < 0):
            p += b2 + px
        else:
            y -=1
            py = twoa2*y
            p += b2 + px - py;


        ellipsePlotPoints(xc, yc, x, y)



    p = round(b2 * (x + 0.5) * (x + 0.5) + a2 * (y - 1) * (y - 1) - a2 * b2)
    while (y > 0):
        y-=1
        py -= twoa2
        if (p > 0):
            p += a2 - py;

        else:
            x +=1
            px += twob2
            p += a2 - py + px


        ellipsePlotPoints(xc, yc, x, y)




def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """

    pt = Point(x, y)
    #pt.draw(win)
    pt.move(500,500) #shifting 0,0 to the right by dx=250, dy=250
    pt.draw(win)

  #  win.getMouse()

def ellipsePlotPoints (xc,yc,x,y):

    time.sleep(0.01)
    PutPixle(win,xc + x, yc + y)
    time.sleep(0.01)

    PutPixle(win,xc - x, yc + y)
    time.sleep(0.01)
    PutPixle(win,xc + x, yc - y)
    time.sleep(0.01)
    PutPixle(win,xc - x, yc - y)

def main():
    a = int(input("Enter semi radius Rx: "))
    b= int(input("Enter semi radius Ry: "))




    ellipse(0,0,a,b)


if __name__ == "__main__":
    main()



