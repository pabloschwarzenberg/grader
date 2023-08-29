def decimal_a_binario(num):
    if num <= 0:
        return "0"
    binario = ""
    while num > 0:
        resto = int(num % 2)
        num = int(num / 2)
        binario = str(resto) + binario
    return binario
num = int(input("Ingresa un número decimal: "))
binario = decimal_a_binario(num)
print("resultado=",binario)