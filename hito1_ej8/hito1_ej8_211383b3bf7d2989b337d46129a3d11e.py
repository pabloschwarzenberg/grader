numero = input("Ingresa un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    descomposicion = ""
    for i, digito in enumerate(numero[::-1]):
        if digito != '0':
            if i == 0:
                descomposicion += digito + "U "
            elif i == 1:
                descomposicion += digito + "D "
            elif i == 2:
                descomposicion += digito + "C "
            elif i == 3:
                descomposicion += digito + "M "

    print("Descomposición:", descomposicion.strip())     