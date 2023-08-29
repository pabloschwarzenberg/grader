#Conversión de Decimal a Binario
numero = int(input("Ingrese un numero: "))
binario = ""
while numero // 2 != 0:
    binario = str(numero % 2) + binario
    numero = numero // 2
print("resultado=",str(numero)+str(binario))    