#Conversión de Decimal a Binario
num = int(input("Ingrese un número decimal"))
binario = " "

while num > 0:
    resto = num%2
    num = num//2
    binario = str(resto) + binario
print("resultado=",binario)


