#Descomponer un número
      # Solicitar al usuario un número de hasta 4 dígitos
numero = input("Ingrese un número de hasta 4 dígitos: ")

# Verificar que el número tenga entre 1 y 4 dígitos
if len(numero) < 1 or len(numero) > 4:
    print("El número ingresado no es válido.")
else:
    # Descomponer el número en unidades, decenas, centenas y miles
    descomposicion = ""
    if len(numero) == 4:
        descomposicion += numero[0] + "M + "
    if len(numero) >= 3:
        descomposicion += numero[-3] + "C + "
    if len(numero) >= 2:
        descomposicion += numero[-2] + "D + "
    descomposicion += numero[-1] + "U"

    # Imprimir la descomposición
    print(descomposicion)
