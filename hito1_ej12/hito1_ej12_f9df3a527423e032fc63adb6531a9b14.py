#Juego adivina mi número
      #Juego_adivina_mi_numero

intentos=5
import random
N=random.randint(1,20)


while intentos>0:
    x= int(input("Adivina un numero entre 1 y 20:",))
    if x>N:
     print("El numero es mayor que", N-1)
     intentos=intentos-1
    if x<N:
     print("El numero es menor que:",N+1)
     intentos=intentos-1

    if x==N:
     print("Adivinaste, mi numero era:",N)
     break 
if x!=N:
    print("No adivinaste, mi numero era:",N)