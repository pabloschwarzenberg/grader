#Juego adivina mi número
#Juego adivina mi número
import random
from random import randint

i=1
j=20

r=random.randint(i,j)




#numero random
#-----------------------------------------


x = int(input("inserte un numero:"))


i = 5


while i > 1:
    


    if x > r:

        i = i - 1
        
        print ("mi numero es mayor")

        x = int(input("n:  ",))

        

    elif x < r:

        i = i - 1
        
        print ("mi numero es menor")

        x = int(input("n:"))


    elif x == r:

        print("Adivinaste, mi número era",r)

        break

    elif i :

        break
    
if i <= 1 :


    if x == r:

        print("Adivinaste, mi número era",r)

    elif x != r:
    
        print ("No adivinaste, mi número era",r)      