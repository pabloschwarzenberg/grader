#ENTRADA
numero = int(input("Ingrese el número decimal:"))

#DESARROLLO
def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

#SALIDA
print("resultado=",(binarizar(numero)))
