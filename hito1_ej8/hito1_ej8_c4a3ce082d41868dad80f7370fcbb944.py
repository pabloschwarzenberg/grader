numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) <= 4 and numero.isdigit():
    numero = numero.zfill(4)  # Rellena con ceros a la izquierda si es necesario

    miles = int(numero[0])
    centenas = int(numero[1])
    decenas = int(numero[2])
    unidades = int(numero[3])

    descomposicion = []

    if miles > 0:
        descomposicion.append(f"{miles}M")
    if centenas > 0:
        descomposicion.append(f"{centenas}C")
    if decenas > 0:
        descomposicion.append(f"{decenas}D")
    if unidades > 0:
        descomposicion.append(f"{unidades}U")

    resultado = " + ".join(descomposicion)
    print(resultado)

else:
    print("Número inválido. Asegúrese de ingresar un número de hasta 4 dígitos.")
