#Factorial!
def Factorial(num):

    count = 1
  
    for i in range(1,num+1):
        count = count * i
      
    print ("The factorial of" , num, " is" )
    print (count)

#Double It! 
def DoubleIt():
    string=input("Please enter a phrase that you would like to 'double':  ")
    output=" "
    for i in string:
        output=output+i+i
    

    print(output)
    

#Camel Case! need help in capitalizing frist char in words
def CamelCase():
    answer=input("please enter a filename:  ")

    answer=answer.title()
    answer=answer.replace(" ","")
    answer=answer.replace(" ","")[0].lower()+answer.replace(" ","")[1:]

    print("your filename should be", answer.replace("/","-"))


def main():
    print("start problem set #2")
    Factorial(9)
    Factorial(17)
    Factorial(25)
    DoubleIt()
    DoubleIt()
    DoubleIt()
    CamelCase()
    CamelCase()
    print("end")
    


main()
    
