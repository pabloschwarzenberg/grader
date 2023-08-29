from random import*
a = randint(0, 20)
b = int(input("ingrese un numero: "))
intentos = 0
while a != b and intentos != 5:
    intentos +=1
    if a > b:
        print("Es mayor")
    else:
        print("Es menor")
    b = input("ingrese otro numero: ")
    b =  int(b)
if a==b and intentos !=5:
    print("Adivinaste, mi número era",a)
if intentos==5:
    print("No adivinaste, mi número era",a)
