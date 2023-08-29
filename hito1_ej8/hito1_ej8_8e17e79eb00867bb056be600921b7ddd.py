numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("Número inválido.")
else:
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) >= 4 else 0

    descomposicion = str(miles) + "M + " + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U"
    print(descomposicion)
