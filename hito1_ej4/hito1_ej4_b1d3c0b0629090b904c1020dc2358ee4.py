#Conversión de Decimal a Binario
n = int(input("Ingrese su valor a convertir:"))
binario = ""
while n > 1 :
    if n % 2 :
        binario += "1"
    else :
        binario += "0"
    n = n //2
if n == 1 :
    binario += "1"
if n == 0 :
    binario += "0"
print("resultado=",binario[::-1])  