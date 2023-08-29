def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    
    descomposicion = ""
    
    if miles > 0:
        descomposicion += str(miles) + "M "
    
    if centenas > 0:
        descomposicion += str(centenas) + "C "
    
    if decenas > 0:
        descomposicion += str(decenas) + "D "
    
    if unidades > 0:
        descomposicion += str(unidades) + "U"
    
    return descomposicion

# Solicitar al usuario un número de hasta 4 dígitos
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Realizar la descomposición del número utilizando la función descomponer_numero
descomposicion = descomponer_numero(numero)

# Imprimir la descomposición del número
print("Descomposición:", descomposicion)