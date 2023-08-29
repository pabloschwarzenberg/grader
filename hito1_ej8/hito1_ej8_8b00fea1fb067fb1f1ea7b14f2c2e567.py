def obtener_valores_lugar(numero):
    miles = numero // 1000
    centenas = numero // 100 % 10
    decenas = numero // 10 % 10
    unidades = numero % 10
    valores_lugar = []
    if miles:
        valores_lugar.append(f"{miles}M")
    if centenas:
        valores_lugar.append(f"{centenas}C")
    if decenas:
        valores_lugar.append(f"{decenas}D")
    if unidades:
        valores_lugar.append(f"{unidades}U")
    return valores_lugar

def main():
    numero = int(input("Ingresa un número de hasta 4 dígitos: "))
    valores_lugar = obtener_valores_lugar(numero)
    print(" + ".join(valores_lugar))

if __name__ == "__main__":
    main()
