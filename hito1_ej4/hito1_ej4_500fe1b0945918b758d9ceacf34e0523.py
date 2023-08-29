def binario(numero):
    b = ''
    while numero // 2 != 0:
        b = str(numero % 2) + b
        numero = numero // 2
    return str(numero) + b

n = int(input("introduzca el numero-> "))
print("resultado =",binario(n))