#Descomponer un número
def descomponer_numero(numero):
    unidades = numero % 10
    decenas = (numero // 10) % 10
    centenas = (numero // 100) % 10
    miles = (numero // 1000) % 10

    descomposicion = []
    if miles > 0:
        descomposicion.append(f"{miles}M")
    if centenas > 0:
        descomposicion.append(f"{centenas}C")
    if decenas > 0:
        descomposicion.append(f"{decenas}D")
    if unidades > 0:
        descomposicion.append(f"{unidades}U")

    return " + ".join(descomposicion)

# Solicitar número al usuario
numero = int(input("Ingrese un número de hasta 4 dígitos: "))

# Descomponer el número
descomposicion = descomponer_numero(numero)

# Imprimir descomposición
print("Descomposición:", descomposicion)
