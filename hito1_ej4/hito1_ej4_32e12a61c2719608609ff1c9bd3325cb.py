def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = binario + str(decimal % 2)
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input())
print("resultado=",binarizar(numero))
