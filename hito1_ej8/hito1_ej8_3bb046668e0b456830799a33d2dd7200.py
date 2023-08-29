#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    numero = numero.zfill(4)
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])

    descomposicion = []
    if miles > 0:
        descomposicion.append(f"{miles}M")
    if centenas > 0:
        descomposicion.append(f"{centenas}C")
    if decenas > 0:
        descomposicion.append(f"{decenas}D")
    if unidades > 0:
        descomposicion.append(f"{unidades}U")

    print(" + ".join(descomposicion))