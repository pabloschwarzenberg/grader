import random  
computador=random.randint(1,20)

i=0
while i<5:
    jugador=int(input("Ingrese un número entre 1 y 20:"))
    if 1>jugador or jugador>20:
        print("Ingrese un número mayor a uno y menor a veinte!!")
    elif jugador<computador and i<5:
        print("Mi número es mayor, inténtalo de nuevo.")
    elif jugador>computador and i<5:
        print("Mi numero es menor inténtelo de nuevo.")
    elif jugador==computador and i<5:
        print("Felicidades ganó el juego")
    i+=1
print("El número era:",computador)