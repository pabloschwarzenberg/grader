def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = numero // 1000
    
    descomposicion = ""
    
    if miles > -1:
        descomposicion += str(miles) + "M+"
    if centenas > -1:
        descomposicion += str(centenas) + "C+"
    if decenas > -1:
        descomposicion += str(decenas) + "D+"
    if unidades > -1:
        descomposicion += str(unidades) + "U"
    
    return descomposicion

numero = int(input("Ingrese un número de hasta 4 dígitos: "))

descomposicion = descomponer_numero(numero)
print("Descomposición:", descomposicion)