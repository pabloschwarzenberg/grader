#Juego adivina mi número
import random
numero=random.randint(1,20)

intentos=5
while intentos>0:
 V=input("ingrese numero:")
 V=int(V)
 
 if V!=numero:
     intentos=intentos-1
     if V<numero:
         print("el numero es mayor")
     if V>numero:
         print("el numero es menor")

 else:
    print ("Adivinaste, mi número era",numero)

if V!=numero:
    intentos=intentos-1
    print("No adivinaste, mi numero era",numero)  