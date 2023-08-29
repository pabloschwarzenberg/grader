#Juego adivina mi número
import random
ns=random.randint(1,20)
intentos=1
while intentos<=5:
    n=int(input("ingresa un numero entre 1 y 20"))
    if n<ns:
        print("El numero que ingresaste es menor que el numero secreto, intenta denuevo")
    elif n>ns:
        print("El numero que ingresaste es mayor que el numero secreto, intenta denuevo")
    elif n==ns:
        break
    intentos=intentos+1
else:
    print("No adivinaste, mi número era",ns)
if n==ns:
  print("Adivinaste, mi numero era",ns)