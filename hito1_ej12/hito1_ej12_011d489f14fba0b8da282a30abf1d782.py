import random

nr = random.randint(1,20)

x= 1

while x<=5:
    
    intento= int(input("adivina numero: "))
                 
    if intento<nr:
        print("mi numero es mayor")
                 
    elif intento>nr:
        print("mi numero es menor")
         
    else:
        
       print("adivinaste, mi numero era ",nr)
       
       break
    
    if x ==5:
       print("no adivinaste,mi numero era ",nr)

    x+= 1



