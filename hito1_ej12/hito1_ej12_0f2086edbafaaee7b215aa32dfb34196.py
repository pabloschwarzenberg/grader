#Juego adivina mi número
import random
s=random.randint(0,20) 
intentos=5
intentos_acabados=True 
n=int(input())

while intentos_acabados and intentos>1:
     if n==s:
        intentos_acabados=False 
     else:
        intentos_acabados=True
        if n>s:
            print(n,"es mayor que el número secreto")
        elif n<s:
            print(n,"es menor que el número secreto")
        intentos=intentos-1
        n=int(input())
           
if n==s:
   print("Adivinaste, mi número era",s)
else:
   print("No adivinaste, mi número era",s)