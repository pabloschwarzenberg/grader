#Juego adivina mi número
 import random
adivinar = random.randint(1,20)
adivinar = 15 
intentos = 1
while intentos <= 5:
    num = int(input("Ingresa un numero entre 1, 5000 "))
    if num == adivinar:
        print("Adivinaste mi numero")
        break
    else:
        intentos += 1
        print("El numero de intentos es: ",str(intentos))
    