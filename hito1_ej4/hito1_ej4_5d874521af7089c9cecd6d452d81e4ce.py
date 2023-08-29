decimal = int(input("Ingrese un número decimal: "))

binario = ""

while decimal > 0:
    residuo = decimal % 2
    binario = str(residuo) + binario
    decimal = decimal // 2

print("Resultado:", binario)