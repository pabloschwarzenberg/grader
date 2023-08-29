import random
numero = random.randrange(1,20)
intento = 0
for i in range(5):
    adivinanza = int(input("Ingrese numero que estoy pensando: "))
    if adivinanza == numero:
        print("Adivinaste, mi número era", numero)
        break
    elif adivinanza > numero:
        print(" Mi número es menor")
    elif adivinanza < numero:
        print(" Mi número es mayor")
    intento += 1
if intento == 5:
    print("No adivinaste, mi número era",numero)