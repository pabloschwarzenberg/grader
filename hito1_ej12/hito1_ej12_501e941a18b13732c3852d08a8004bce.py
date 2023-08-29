import random
magia = random.randint(0,20)
intentos = 5
seguir = True
while(seguir):
    numero = int(input("ingresa el número: "))
    if(numero == magia):
        print("adivinaste, mi numero era",magia)
        seguir = False
    elif(numero > magia):
        print("el número ingresado es mayor que el número secreto")
        intentos = intentos-1
    elif(numero < magia):
        print("el número ingresado es menor que el número secreto")
        intentos = intentos-1
    if(intentos==0):
        print("No adivinaste, mi numero era",magia)
        break
        