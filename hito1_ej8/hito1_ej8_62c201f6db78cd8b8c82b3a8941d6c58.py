numero = input("Ingresa un número de hasta 4 dígitos: ")

# Asegurarse de que el número tenga como máximo 4 dígitos
if len(numero) > 4:
    print("Error: El número debe tener como máximo 4 dígitos.")
else:
    # Rellenar con ceros a la izquierda si el número tiene menos de 4 dígitos
    numero = numero.zfill(4)
    
    miles = int(numero[0])
    centenas = int(numero[1])
    decenas = int(numero[2])
    unidades = int(numero[3])
    
    descomposicion = ""
    
    if miles > 0:
        descomposicion += str(miles) + "M + "
    if centenas > 0:
        descomposicion += str(centenas) + "C + "
    if decenas > 0:
        descomposicion += str(decenas) + "D + "
    descomposicion += str(unidades) + "U"
    
    print("Descomposición:", descomposicion)

      