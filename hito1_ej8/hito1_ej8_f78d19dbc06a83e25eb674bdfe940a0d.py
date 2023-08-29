numero = input("Ingresa un número de hasta 4 dígitos: ")

# Verificar que el número tenga hasta 4 dígitos
if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    # Completar con ceros a la izquierda si el número tiene menos de 4 dígitos
    numero = numero.zfill(4)
    
    # Obtener cada dígito del número
    unidades = int(numero[3])
    decenas = int(numero[2])
    centenas = int(numero[1])
    miles = int(numero[0])
    
    # Construir la descomposición en formato de cadena
    descomposicion = ''
    if miles > 0:
        descomposicion += str(miles) + 'M + '
    if centenas > 0:
        descomposicion += str(centenas) + 'C + '
    if decenas > 0:
        descomposicion += str(decenas) + 'D + '
    if unidades > 0:
        descomposicion += str(unidades) + 'U'
    
    # Imprimir la descomposición
    print("La descomposición del número es:", descomposicion)

      