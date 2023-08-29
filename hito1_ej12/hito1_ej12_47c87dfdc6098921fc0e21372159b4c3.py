import random
intentos=0
ganaste=0
secreto = random.randint(1,20)
while intentos<5:
    num = int(input("Ingrese su intento -> "))
    if num == secreto:
        ganaste=1
        print("Adivinaste, mi número era",secreto)
        
    if num < secreto:
        print("mi número es mayor")

    if num > secreto:
        print("mi número es menor")
    intentos=intentos+1
    if intentos==5 and ganaste==0:
        print ("No adivinaste, mi número era",secreto)