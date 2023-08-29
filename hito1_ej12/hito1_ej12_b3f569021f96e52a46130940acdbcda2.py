#Juego adivina mi número
intentos=5
import random
n= random.randint(1,20)
while intentos>=1:
    a=int(input("ingrese un numero:"))
    if n>a:
        print("el numero que escojiste es menor")
        intentos=intentos-1
    elif n<a:
        print("el numero que escogiste es mayor ")
        intentos=intentos-1
    elif n==a:
        print("adivinaste, mi numero era:",n)
        break

else :
     print(" no adivinaste, mi numero era:",n)
     