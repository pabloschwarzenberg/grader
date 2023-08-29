#Descomponer un número

# Recibimos la entrada del usuario
num = int(input("Ingrese un número de hasta 4 dígitos: "))

# Verificamos que el número no tenga más de 4 dígitos
if num > 9999 or num < 0:
    print("Número inválido. Debe tener hasta 4 dígitos y ser positivo.")
else:
    # Obtenemos las unidades, decenas, centenas y miles
    unidades = num % 10
    num = num // 10

    decenas = num % 10
    num = num // 10

    centenas = num % 10
    num = num // 10

    miles = num % 10

    # Imprimimos la descomposición del número
    print(str(miles) + "M + " + str(centenas) + "C + " + str(decenas) + "D + " + str(unidades) + "U") 