#Juego adivina mi número
import random
intento=5
numero=random.randint(1,20)
print("ADIVINA EL NÚMERO!")
while intento > 0:
    num=int(input("Ingresa el número que creas:"))
    if num<numero:
        print("mi número es mayor")
        intento=intento-1
    elif num>numero:
        print("mi número es menor")
        intento=intento-1
    elif num==numero:
        print("FELICIDADES!!, HAS ACERTADO")
        break
if intento == 0:
    print("intentos agotados")