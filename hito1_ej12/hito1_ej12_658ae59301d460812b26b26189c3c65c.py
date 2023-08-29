import random
v2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
numero = int('{}'.format(v2[random.randint(0,20)]))
contador = 0
print(numero)
while contador < 5:
    jugador = int(input("Ingresa un numero:"))
    contador = (contador + 1)
    if jugador < numero:
        print("mi numero es mayor")
    if jugador > numero:
        print("mi numero es menor")
    if jugador == numero:
        print("Adivinaste, mi numero era", numero)
        break
else:
    print("No adivinaste, mi numero era", numero)



