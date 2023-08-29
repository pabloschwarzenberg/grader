from random import randint
numero = randint(0,20)
intentosRealizados = 0
print("Bueno, estoy pensando un número entre el 1 y el 20.")
estimacion = int(input(""))
while intentosRealizados < 6:
    if 0<=estimacion<=20:
        if estimacion < numero:
            print("mi número es mayor")
        elif estimacion > numero:
            print("mi número es menor")
        else:
            print("Adivinaste, mi número era "+str(numero))
            break
        intentosRealizados += 1
        estimacion = 0
    else:
        print("Ingrese solo números")
if intentosRealizados == 5:
    print("No adivinaste, mi nùmero era " + str(numero))