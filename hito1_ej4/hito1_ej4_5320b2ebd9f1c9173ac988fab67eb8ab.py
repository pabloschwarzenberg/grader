numero = int(input("Ingrese un número decimal: "))
binario = ""
while numero > 0:
    binario = str(numero % 2) + binario
    numero = numero // 2
print("resultado={}".format(binario))
