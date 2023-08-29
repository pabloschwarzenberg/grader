import random
n=random.randint(1,20)
print(n)
intento=5
numero_incorrecto=True
numero=input("ingrese numero: ")
numero=int(numero)
while numero_incorrecto and intento>1:
    if numero==n:
     numero_incorrecto=False
     print("Adivinaste, mi numero era: ",n)
    else:
        numero_incorrecto=True
        intento=intento-1
        if int(numero)<n:
            print("El numero ingresado es menor")
        elif int(numero)>n:
            print("El numero ingresado es mayor")
    numero=input("ingrese numero: ")
if numero==n:
    print("Adivinaste, mi numero era: ",n)
else:
    print("No adivinaste, mi numero era: ",n)
