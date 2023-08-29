#Juego adivina mi número
from random import randint
n = randint(1,20)
while True:
    a = int(input("Escoge un numero:"))
    if(n == a):
        print("Adivinaste,mi número era:",n)
        break
    if(n < a):
        print("Mi número es menor")
          
    elif(n > a):
        print("Mi número es mayor")

    print("SEGUNDO INTENTO")

    a = int(input("Escoge un numero:"))

    if(n == a):
        print("Adivinaste, mi número era:",n)
        break
    if(n < a):
        print("Mi número es menor")
    elif(n > a):
        print("Mi número es mayor")

    print("TERCER INTENTO")

    a = int(input("Escoge un numero:"))
    if(n == a):
        print("Adivinaste,mi número era:",n)
        break
    if(n < a):
        print("Mi número es menor")
          
    elif(n > a):
        print("Mi número es mayor")

    print("CUARTO INTENTO")

    a = int(input("Escoge un numero:"))
    if(n == a):
        print("Adivinaste,mi número era:",n)
        break
    if(n < a):
        print("Mi número es menor")
          
    elif(n > a):
        print("Mi número es mayor")

    print("QUINTO INTENTO")

    a = int(input("Escoge un numero:"))
    if(n == a):
        print("Adivinaste,mi número era:",n)
        break
    if(n < a):
        print("Mi número es menor")
          
    elif(n > a):
        print("Mi número es mayor")

    else:
        print("No adivinaste, mi número era:",n)
        break
        