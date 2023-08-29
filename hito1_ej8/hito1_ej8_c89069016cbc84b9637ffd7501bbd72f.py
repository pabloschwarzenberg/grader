numero = input("Ingrese un número de hasta 4 dígitos: ")

# Validar que el número ingresado tenga hasta 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Rellenar el número con ceros a la izquierda si tiene menos de 4 dígitos
    numero = numero.zfill(4)

    # Obtener los dígitos individuales del número
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    # Crear la representación de la descomposición
    descomposicion = ""
    if miles > 0:
        descomposicion += f"{miles}M + "
    if centenas > 0:
        descomposicion += f"{centenas}C + "
    if decenas > 0:
        descomposicion += f"{decenas}D + "
    descomposicion += f"{unidades}U"

    # Mostrar la descomposición
    print("Descomposición del número:")
    print(descomposicion)
