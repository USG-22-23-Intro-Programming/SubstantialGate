#Currency Converter

def currencyConverter():
    print("Welcome to currency converter")
    print("  ")
    name={"1 : United States dollar": 1.00,
          "2 : Singapore dollar": 1.40,
          "3 : New Zealand dollar":1.96 ,
          "4 : Jamaican dollar": 153.91}

    
    listOfKeys=name.keys()
    listOfKeys=list(listOfKeys)

    for key in listOfKeys:
        print(key)
    country=input("Please enter which type of currency you have, Choose from the list: ")
    country=float(country)
    print("  ")
    money=input("Please enter how much money you have: ")
    z=float(money)
    print("  ")
    for key in listOfKeys:
        print(key)
    currency=input("Please enter which type of currency you would like to convert to. choose from the list: ")
    currency=float(currency)

    x=1
    if country==1:
        x=1.00
    if country==2:   
        x=1.40
    if country==3:
        x=1.69
    if country==4:
        x=153.91
    y=1
    if currency==1:
        y=1.00
    if currency==2:   
        y=1.40
    if currency==3:
        y=1.69
    if currency==4:
        y=153.91
    print(" - - - - calculating - - - - ")
    print("  ")
    print("You have", float((y/x)*z),"dollar")
    print("  ")

    

  
#Grocery List!
def groceryList(food):
 
    groceries = {"apple": 1.50,
     "orange": 1.00,
     "banana":1.00,
     "bagel": 1.25,
     "cabbage": 1.50,
     "spinach":4.25,
     "milk": 2.75,
     "eggs":3.25,
     "cake": 8.00,
     "pasta":3.50}
    eishaJaein=0
    for i in range(len(food)):
        f=groceries.get(food[i])
        eishaJaein=eishaJaein+float(f)
    print("You have purchased", food)
    print("Your total is " + str(eishaJaein), "dollars")

    
def main():
    currencyConverter()
    currencyConverter()
    currencyConverter()
    groceryList(['apple','bagel','cabbage','milk',])
    groceryList(['cake','bagel','bagel','milk','bagel','bagel','bagel','bagel',])

if __name__ == "__main__":
    main()






