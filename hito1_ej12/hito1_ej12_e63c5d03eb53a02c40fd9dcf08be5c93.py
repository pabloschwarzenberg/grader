#Juego adivina mi número
import random
numero = random.randint(1,20)
n=-5
intento=0
while n!=numero and intento<5:
    n=int(input("número: "))
    if n>numero:
        print("mi número es menor")
    if n<numero:
        print("mi número es mayor")
    intento+=1
if numero==n:
    print("Adivinaste, mi número era "+str(numero))
else:
    print("No adivinaste, mi número era "+str(numero))


