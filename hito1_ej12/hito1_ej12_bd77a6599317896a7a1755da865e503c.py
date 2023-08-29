import random

numero = random.randint(1,20)
intentos = 5

jugando = True

print("ADININA UN NUMERO DEL 1 A 20")

while jugando:
    
    intentos += 1
    
    if intentos <=5:
        eleccion = int(input("Dime un numero: "))
        if eleccion == numero:
            print("has acertado. has necesitado", intentos, "intentos.")
            jugando = False
        elif eleccion > numero:
            print("Demasiado alto. llebas", intentos, "intentos.")
        elif eleccion < numero:
            print("Demasiado bajo. llevas", intentos, "intentos.")
            
    else:
        print("Se te acabaron los intentos. has perdidos")
        jugando = False