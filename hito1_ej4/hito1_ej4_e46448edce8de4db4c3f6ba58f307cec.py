def decimal_a_binario(codigo):
    if codigo <= 0:
        return "0"
    binario = ""
    while codigo > 0:
        residuo = int(codigo % 2)
        codigo = int(codigo / 2)
        binario = str(residuo) + binario
    return binario
codigo = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(codigo)
print("resultado=",binario)