#Descomponer un número
numero = int(input("Ingrese numero: "))
descomponer = numero
digitos = []
largo = len(str(numero))
contador = largo
cadena = ''

for i in range(largo):
    digitos.append(descomponer // (10 ** (contador-1)))
    descomponer %= (10 ** (contador-1))
    contador -= 1

if largo == 4:
    for i in range(4):
        if i == 0:
            cadena += str(digitos[i]) + 'M'
        else:
            cadena += " + " + str(digitos[i])
            if i == 1:
                cadena += 'C'
            elif i == 2:
                cadena += 'D'
            else:
                cadena += 'U'
elif largo == 3:
    for i in range(3):
        if i == 0:
            cadena += str(digitos[i]) + 'C'
        else:
            cadena += " + " + str(digitos[i])
            if i == 1:
                cadena += 'D'
            elif i == 2:
                cadena += 'U'

elif largo == 2:
    for i in range(2):
        if i == 0:
            cadena += str(digitos[i]) + 'D'
        else:
            cadena += " + " + str(digitos[i])
            cadena += 'U'
else:
    cadena += str(digitos[0]) + 'U'

print(cadena)
