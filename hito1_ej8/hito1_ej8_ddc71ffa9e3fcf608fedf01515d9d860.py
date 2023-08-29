#Descomponer un número
numero = input("Ingresa un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("Número inválido. Por favor, ingresa un número de hasta 4 dígitos.")
else:
    descomposicion1 = ""
    descomposicion2 = ""
    descomposicion3 = ""
    descomposicion4 = ""
    for i in range(len(numero)):
        digito = int(numero[i])
        posicion = len(numero) - i

        if digito != 0:
            if posicion == 4:
                descomposicion4 += str(digito) + "M"
            elif posicion == 3:
                descomposicion3 += str(digito) + "C"
            elif posicion == 2:
                descomposicion2 += str(digito) + "D"
            elif posicion == 1:
                descomposicion1 += str(digito) + "U"

    print(descomposicion4 +"+"+ descomposicion3 +"+"+ descomposicion2 +"+"+ descomposicion1)