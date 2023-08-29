numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("Error: El número ingresado tiene más de 4 dígitos.")
else:
    descomposicion = ""

    for i, digito in enumerate(numero):
        if digito != '0':
            if len(numero) - i == 4:
                descomposicion += digito + "M + "
            elif len(numero) - i == 3:
                descomposicion += digito + "C + "
            elif len(numero) - i == 2:
                descomposicion += digito + "D + "
            elif len(numero) - i == 1:
                descomposicion += digito + "U"

    print("Descomposición:", descomposicion)

      