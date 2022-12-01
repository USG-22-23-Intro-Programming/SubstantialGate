from graphics import*
from Button import*


def main():

    win = GraphWin("Palindrome", 800, 600)
    win.setBackground("mistyrose1")

    Q = Button(win, Point(600, 500), Point(700, 575), "indianred1", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "lightcoral", "Check!")

    E = Entry(Point(400, 300), 30)
    E.draw(win)

    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential Palindrome below!")
    T.draw(win)
    

    while True:
        a=True
        

        m = win.getMouse()

        if Q.isClicked(m):
            break

        if Check.isClicked(m):
            pal = E.getText()

        length = len(pal)
        for i in range(length):
            if pal[i] != pal[length - 1 - i]:
                a=False
        if a==False:
            T.setText("No, this is not a palindrome")
        if a==True:
            T.setText("Yes, this is a palindrome")



            ''''if pal[i]==pal[length-1-i]:
                T.setText("Yes, this is a palindrome")
            
            s = pal

            length = len(s)
            for i in range(length):
                if s[i] != s[length - 1 - i]:
                    A=T
                else:
                    A=F
        if A==T:
            T.setText("No, this is not a palindrome")
        else:
            T.setText("Yes, this is a palindrome")

   
            for i in range(length):
                if s[i] != s[length - 1 - i]:
                    return False
        
            return True
            while False:
                T.setText("No, this is not a palindrome")
            while True:
                T.setText("Yes, this is a palindrome")
            
            
        for i in range(len(pal)):
            if pal[i] != pal[len(pal) - 1 - i]:
                a=True
            else:
                a=False
        while a==True:
            T.setText("Yes, this is a palindrome")
        while a==False:
            T.setText("No, this is not a palindrome") '''
            
                    
    win.close()


if __name__ == "__main__":
    main()
