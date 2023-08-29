numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4 or not numero.isdigit():
    print("Número inválido. Asegúrese de ingresar un número de hasta 4 dígitos.")
else:
    numero = numero.zfill(4)
    miles = int(numero[0])
    centenas = int(numero[1])
    decenas = int(numero[2])
    unidades = int(numero[3])
    descomposicion = ""
    if miles > 0:
        descomposicion += f"{miles}M "
    if centenas > 0:
        descomposicion += f"{centenas}C "
    if decenas > 0:
        descomposicion += f"{decenas}D "
    if unidades > 0:
        descomposicion += f"{unidades}U "
    print("Descomposición:", descomposicion)
