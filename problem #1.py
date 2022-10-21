'''print("hello world!")

answer=input("what is your name?")
print("hello "+answer)

x=10
print(x)

weekday = False

if weekday:
    print("it is a weekday")
else:
    print("it is a weekend")

x=5 "set x equal to 5"
x==5 "is x equal to 5?" conditions
'''

    
#Greeting!
    
def greeting():
    answer=input("Please enter your name:  ")
    print("Nice to meet you! "+answer+", I'm Jaein, have a good day!")

#IsMultiple!
 
def ismultiple(x,y):
# % is mod
    if (x%y==0):
        print(int(x), " is a multiple of ", int(y))
    else:
        print(int(x), " is not a multiple of " , int(y))


#Palindrome!
    
def palindrome():
    s=input("please enter a potential palindrome: ")
    length=len(s)
    #for loop to repeat
    #i start at 0 and it's add one each time
    # ! is "not equal"
    for i in range(length):
        if s[i]!=s[length-1-i]:
            return False
        
        
            return True
        

'''def palindrome():
    s=input("please enter a potential palindrome: ")
    if s[::-1]==s:
        print("Fantasic!", s , "is a palindrome")
    else:
        print("Unfortuately,", s , "is not a palindrome")
    # when you do a[::-1], it starts from the end towards, So it reverses a.
    # if s == s[::-1]:'''
        

#creating method

def main():
    greeting()
    ismultiple(20,3)
    ismultiple(81,9)
    ismultiple(99,99)
    answer=palindrome()
    print(answer)

main()
        
