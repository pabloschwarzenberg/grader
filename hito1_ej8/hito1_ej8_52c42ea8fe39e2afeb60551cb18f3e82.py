numero = input("Ingrese un número de hasta 4 dígitos: ")

# Asegurarse de que el número tenga máximo 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Obtener cada dígito por separado
    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) >= 4 else 0

    # Imprimir la descomposición
    descomposicion = []
    if miles > 0:
        descomposicion.append(str(miles) + "M")
    if centenas > 0:
        descomposicion.append(str(centenas) + "C")
    if decenas > 0:
        descomposicion.append(str(decenas) + "D")
    if unidades > 0:
        descomposicion.append(str(unidades) + "U")

    resultado = " + ".join(descomposicion)
    print("Descomposición:", resultado)
      