decimal = int(input("Ingresa un número decimal: "))

def deci_(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = int(decimal % 2)
        decimal = int(decimal / 2)
        binario = str(residuo) + binario
    return binario

binario = deci_(decimal)

print("El número ",decimal, "es ",binario," en binario")