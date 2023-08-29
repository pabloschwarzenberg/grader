#Conversión de Decimal a Binario
numero = float(input())
numero_bin = bin(int(numero))
print("resultado=" + numero_bin[2:])