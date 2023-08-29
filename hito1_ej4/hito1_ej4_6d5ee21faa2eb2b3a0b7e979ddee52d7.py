#Conversión de Decimal a Binario
numero = int(input("Ingrese numero"))
binario = ""
while numero > 1:
    if numero%2 == 0:
        binario = binario + "0"
    else:
        binario = binario + "1"
    numero = int(numero / 2)  
binario = binario + "1"
print("resultado=",binario[::-1])           