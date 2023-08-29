decimal = int(input("ingrese numero decimal: "))
binario = 0
contador = 0
temp = decimal
while temp > 0:
    binario = ((temp%2)*(10**contador)) + binario
    temp = int(temp/2)
    contador += 1      
print("resultado = ", binario)