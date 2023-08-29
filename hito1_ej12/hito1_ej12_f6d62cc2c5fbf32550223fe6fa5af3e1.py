#Juego adivina mi número
import random 
x=(random.randint(1,20))
intentos=0
while intentos<=5:
        A=int(input("vuelve a intentarlo:"))
        intentos=intentos+1
        if A==x:
           print("adivinaste el numero")
           break
        elif A<x:
           print("el numero ingresado es menor al se intenta adivinar")
        elif A>x:
           print("el numero ingresado es mayor al que se intenta adivinar")
        if intentos==5:
           print("limite de intentos alcanzado")
           break