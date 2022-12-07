from graphics import*
from Button import*
import time

#I have one problem when i click something before grayscale,
#grayscale is not fully gray, yello sometimes show ups
#solution : get average for RGB and make that a value for new RGB

def darken(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red=pix[0]
            green=pix[1]
            blue=pix[2]
            if red-25>0:
                red=red-25
            if red<25:
                red=0
            if green-25>0:
                green=green-25
            if green<25:
                green=0
            if blue-25>0:
                blue=blue-25
            if blue<25:
                blue=0
        
                
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def lighten(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            if red+25<230:
                red=red+25
            if red>230:
                red=255
            if green+25<230:
                green=green+25
            if green>230:
                green=255
            if blue+25<230:
                blue=blue+25
            if blue>230:
                blue=255

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def grayScale(img):
    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            n=(red+green+blue)/3
            n=round(n)
            red=n
            green=n
            blue=n
            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)

def contrast(img):
    #you are making light pixel(not single RGB value) lighter and dark pixel darker.

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            red = pix[0]
            green = pix[1]
            blue = pix[2]
            A=red+green+blue
            if A>382:
                #light color, make it lighter
                if red<230:
                    red=red+25
                if red>=230:
                    red=255
                if green<230:
                    green=green+25
                if green>=230:
                    green=255
                if blue<230:
                    blue=blue+25
                if blue>=230:
                    blue=255
            if A<=382:
                #dark color, make it darker
                if red>25:
                    red=red-25
                if red<=25:
                    red=0
                if green>25:
                    green=green-25
                if green<=25:
                    green=0
                if blue>25:
                    blue=blue-25
                if blue<=25:
                    blue=0
                
            '''if red>128:
                red=red+50
            if red>205:
                red=255
            if red<128:
                red=red-50
            if red<50:
                red=0
            if green>128:
                green=green+50
            if green>205:
                green=255
            if green<128:
                green=green-50
            if green<50:
                green=0
            if blue>128:
                blue=blue+50
            if blue>205:
                blue=255
            if blue<128:
                blue=blue-50
            if blue<50:
                blue=0'''

            c = color_rgb(red, green, blue)
            img.setPixel(i, j, c)
'''def restart():
    if B5.isClicked(m):
        win = GraphWin("Image Editor", 800, 600)
        win.setBackground("palegreen4")
        

        I = Image(Point(330, 340), "soccer.png")
        I.draw(win)

        B = Button(win, Point(650, 75), Point(750, 150), "darkseagreen4", "Darken")
        B2 = Button(win, Point(650, 175), Point(750, 250), "darkseagreen3", "Lighten")
        B3 = Button(win, Point(650, 275), Point(750, 350), "darkseagreen2", "Grayscale")
        B4 = Button(win, Point(650, 375), Point(750, 450), "darkseagreen1", "Contrast")
        B5= Button(win, Point(100, 50), Point(550, 80), "darkseagreen1", "Welcome to image editor!")

        Q = Button(win, Point(650, 475), Point(750, 550), "darkseagreen", "QUIT")
    if Q.isClicked(m):
        win.close()'''
 
        

        
def main():

    win = GraphWin("Image Editor", 800, 600)
    win.setBackground("palegreen4")

    I = Image(Point(330, 340), "soccer.png")
    I.draw(win)

    B = Button(win, Point(650, 75), Point(750, 150), "darkseagreen4", "Darken")
    B2 = Button(win, Point(650, 175), Point(750, 250), "darkseagreen3", "Lighten")
    B3 = Button(win, Point(650, 275), Point(750, 350), "darkseagreen2", "Grayscale")
    B4 = Button(win, Point(650, 375), Point(750, 450), "darkseagreen1", "Contrast")
    B5= Button(win, Point(100, 50), Point(550, 80), "darkseagreen1", "Welcome to image editor!")

    Q = Button(win, Point(650, 475), Point(750, 550), "darkseagreen", "QUIT")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayScale(I)

        if B4.isClicked(m):
            contrast(I)

            

        if Q.isClicked(m):
            break

    win.close()

            

            

            



if __name__ == "__main__":
    main()
