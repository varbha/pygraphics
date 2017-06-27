from graphics import *
import time

def MidpointCircle(r):
    win = GraphWin('MidPoint Circle Algorithm', 500, 500)
   # win.setBackground('cyan')
    win.yUp() #inverting the default coordinates to set 0,0 as the default at the lower left corner of the dialog box



    x=0
    y=r
    h=1-r #hstart



    print("(x,y): ",x,y)
    print("h:",h)



    #time.sleep(0.1)
    #PutPixle(win, x, y)
    xprev = 0
    yprev = r
    while(y>x):

        if h<0:
            #select the east point
            x = x + 1

            time.sleep(0.01)
            PutPixle(win, x, y)
            PutPixle(win, y, x)
            PutPixle(win, y, -x)
            PutPixle(win, x, -y)
            PutPixle(win, -y, x)
            PutPixle(win, -x, -y)
            PutPixle(win, -y, -x)
            PutPixle(win, -x, y)
            PutPixle(win, -y, x)

            h=h+2*xprev+3 #hnew based on east pixel
            xprev=xprev+1# recalculating previous value of x to be used for next calculation of hnew


        else:
            #select the south east point
            y = y - 1
            x = x + 1

            time.sleep(0.01)
            PutPixle(win, x, y)
            PutPixle(win, y, -x)
            PutPixle(win, y, x)
            PutPixle(win, x, -y)
            PutPixle(win, -y, x)
            PutPixle(win, -x, -y)
            PutPixle(win, -y, -x)
            PutPixle(win, -x, y)
            PutPixle(win, -y, x)

            h=h+2*(xprev-yprev)+5 #hnew based on south east pixel
            yprev = yprev - 1 #recalculating previous values of x and y to be used for next calculation of hnew
            xprev=xprev+1




        print("(x,y): ", x, y)
        print("h:", h)

    time.sleep(10)
    win.close()



def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    #pt.draw(win)
    pt.move(250,250) #shifting 0,0 to the right by dx=250, dy=250
    pt.draw(win)

  #  win.getMouse()

def main():
    r = int(input("Enter radius R: "))


    MidpointCircle(r)


if __name__ == "__main__":
    main()






