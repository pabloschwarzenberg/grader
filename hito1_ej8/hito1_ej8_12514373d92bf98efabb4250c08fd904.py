#Descomponer un número
numero = input("Ingrese un número de hasta 4 dígitos: ")

if len(numero) > 4:
    print("El número ingresado tiene más de 4 dígitos.")
else:
    descomposicion = ""
    longitud = len(numero)
    
    # Descomposición en unidades, decenas, centenas y miles
    if longitud == 4:
        descomposicion += numero[0] + "M + "
    if longitud >= 3:
        descomposicion += numero[-3] + "C + "
    if longitud >= 2:
        descomposicion += numero[-2] + "D + "
    descomposicion += numero[-1] + "U"
    
    print("Descomposición:", descomposicion)
      