#Juego adivina mi número
from random import *
juegos=1
incognita=randint(1,20)

while juegos<=5:
    juegos+=1
    var=int(input("ingresa un numero del 1 al 20:\n"))
    if var==incognita:
        print("Adivinaste, mi número era",(incognita))
        juegos=7
    else:
        if var<incognita:
            print("mi número es mayor")
        else:
            print("mi número es menor")
            
if juegos==6:
     print("No adivinaste, mi número era",(incognita))     