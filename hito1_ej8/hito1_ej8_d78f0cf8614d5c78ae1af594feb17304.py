#Descomponer un número
def descomponer_numero(numero):
    descomposicion = []
    
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10
    
    if miles > 0:
        descomposicion.append(str(miles) + "M")
    if centenas > 0:
        descomposicion.append(str(centenas) + "C")
    if decenas > 0:
        descomposicion.append(str(decenas) + "D")
    if unidades > 0:
        descomposicion.append(str(unidades) + "U")
    
    return " + ".join(descomposicion)


numero = int(input("Ingresa un número de hasta 4 dígitos: "))
descomposicion = descomponer_numero(numero)
print("Descomposición:", descomposicion)
