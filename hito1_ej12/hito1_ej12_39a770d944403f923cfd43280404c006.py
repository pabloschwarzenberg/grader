import random as rnd
n = rnd.randrange (1,20)

cont= 5
while cont > 0:
    print("Adivina el numero, tienes ",cont,"intentos para adivinar: ")
    intento=int(input())
    if intento == n:
        print("Adivinaste, mi numero era",n)
        cont=0
    elif cont == 1:
        print("No adivinaste, mi número era",n)
        cont = cont-1
    elif intento > n:
        print("El numero es menor")
        cont = cont-1
    elif intento < n:
        print("El numero es mayor")
        cont = cont-1