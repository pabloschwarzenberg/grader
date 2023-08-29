import random

numero_intento=1
min=1
max=20
numero = random.randint(min, max)

print("Bienvenidos a Adivina el número")
print()

while numero_intento<=5:
    intento=int(input("Ingrese un número: "))
    numero_intento += 1

    if intento < numero:
        print("Mi número es mayor")
    if intento > numero:
        print("Mi número es menor")
    if intento == numero:
        break

if intento == numero:
    print("Adivinaste, mi número era " + str(numero))