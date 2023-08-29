import random
intentos_realizados = 0
numero = random.randint(1,20)
while intentos_realizados < 6:
    print("Ingrese un número")
    x = input()
    x = int(x)
    if x < numero:
        print("mi número es mayor")
    if x > numero:
        print("mi número es menor")
    if x == numero:
        break
if x == numero:
    print("Adivinaste, mi número era", numero)
else:
    print("No adivinaste, mi número era", numero)      