#Juego adivina mi número
import random
n=int(random.randint(1,20))
intentos=5

while intentos>0 :
 n_jugador=input()
 if int(n)<int(n_jugador) :
     print("Tu numero es menor")
 elif int(n)>int(n_jugador) :
     print("Tu numero es mayor")
 elif int(n)==int(n_jugador) :
     print("Adivinaste, mi numero era",n)
 intentos=intentos-1
if intentos==0 :
     print("No adivinaste, mi numero era",n)
      