#Juego adivina mi número
from random import randint, uniform,random
n = randint(1,20)
i = 1
while(i != 6):
    print("intento",i)
    a= int(input("Adivina: "))
    if a == n:
        print("Adivinaste, mi número era ",n)
        break
    elif a > 0 and a <= 20:
        if a > n:
            print("mi numero es menor")
            i = i + 1
        
        elif a < n:
            print("mi numero es mayor")
            i = i + 1
else:
  print("No adivinaste, mi número era",n)