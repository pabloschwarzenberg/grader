#Descomponer un número
def descomponer_numero(numero):
    descomposicion = []
    if numero >= 1000:
        miles = numero // 1000
        descomposicion.append(f"{miles}M")
        numero %= 1000
    if numero >= 100:
        centenas = numero // 100
        descomposicion.append(f"{centenas}C")
        numero %= 100
    if numero >= 10:
        decenas = numero // 10
        descomposicion.append(f"{decenas}D")
        numero %= 10
    unidades = numero
    descomposicion.append(f"{unidades}U")

    return " + ".join(descomposicion)

numero = int(input("Ingresa un número de hasta 4 dígitos: "))
descomposicion = descomponer_numero(numero)
print(descomposicion)
