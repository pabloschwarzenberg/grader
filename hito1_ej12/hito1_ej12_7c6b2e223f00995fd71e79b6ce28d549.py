import random

numero_s=random.randint(1,20)
correcto=False
intento=0
while correcto==False and intento!=5:
    numero=int(input("Ingresa un numero: "))
    if numero<numero_s:
        print("mi numero es mayor que ",numero)
    if numero>numero_s:
        print("mi numero es menor que ",numero)
    if numero==numero_s:
        print("Adivinaste, mi número era: ",numero_s)
        correcto=True
    intento+=1

if correcto==False:
    print("No adivinaste, mi número era: ",numero_s)