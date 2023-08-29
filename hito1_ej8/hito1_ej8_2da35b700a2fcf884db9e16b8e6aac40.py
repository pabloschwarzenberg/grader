#Descomponer un número
valido = False
numero = ""
while valido == False:
    numero = input("Ingrese Numero hasta 4 digitos")
    if len(numero) <= 4:
        valido = True
listaNumero = list(numero)
i = len(listaNumero) - 1
cadena = []
indiceDescomposicion = 4
while i >= 0:
    if indiceDescomposicion == 4:
       cadena.append(listaNumero[i] + "U")
    elif indiceDescomposicion == 3:
       cadena.append(listaNumero[i] + "D")
    elif indiceDescomposicion == 2:
       cadena.append(listaNumero[i] + "C")
    else:
       cadena.append(listaNumero[i] + "M")
    indiceDescomposicion -= 1
    i -= 1
i = len(cadena) - 1
output = ""
while i >= 0:
    if i == 0:
        output = output + cadena[i]
    else:
        output = output + cadena[i] + "+"
    i -= 1
print(output)