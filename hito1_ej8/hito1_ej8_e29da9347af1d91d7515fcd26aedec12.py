numero = input("Ingrese un número de hasta 4 dígitos: ")


if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
   
    numero = numero.zfill(4)

   
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    # Mostrar la descomposición del número
    print("Unidades:", unidades)
    print("Decenas:", decenas)
    print("Centenas:", centenas)
    print("Miles:", miles)
