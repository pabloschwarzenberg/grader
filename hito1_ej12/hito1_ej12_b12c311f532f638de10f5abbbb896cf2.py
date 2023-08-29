#Juego adivina mi número
import random

n1=int(input("esccriba un numero entre 1 a 20: "))

n=random.randint(1,20)

c=1

while c<=5:
    if n1 < n:
        print("mi numero es mayor")
        n1=int(input("ingrese nuevamente: "))
        c=c+1
    elif  20 > n1 > n:
        print("mi numero es menor")
        n1=int(input("ingrese nuevamente: "))
        c=c+1
    elif n1==n:
        print("adivinaste mi numero, era: ",n)
        break
    elif n1 > 20:
        print("error: el numero ingresado es mayor que 20")
        break
    else:
        print("no adivinaste mi numero era",n)
        break