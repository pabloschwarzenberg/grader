numero = input("Ingrese un número de hasta 4 dígitos: ")


if len(numero) > 4 or not numero.isdigit():
    print("El número ingresado no es válido.")
    
else:

    unidades = int(numero[-1])
    decenas = int(numero[-2]) if len(numero) >= 2 else 0
    centenas = int(numero[-3]) if len(numero) >= 3 else 0
    miles = int(numero[-4]) if len(numero) == 4 else 0

    descomposicion = ''
    if miles > 0 or (miles == 0 and len(numero) == 1):
        descomposicion += str(miles) + 'M + '
    if centenas > 0 or (centenas == 0 and len(numero) == 2):
        descomposicion += str(centenas) + 'C + '
    if decenas > 0 or (decenas == 0 and len(numero) == 3):
        descomposicion += str(decenas) + 'D + '
    if unidades > 0 or (unidades == 0 and len(numero) == 4):
        descomposicion += str(unidades) + 'U'
        
    print(descomposicion)
