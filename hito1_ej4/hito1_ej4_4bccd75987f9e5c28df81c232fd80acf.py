#Conversión de Decimal a Binario
numero = eval(input("Ingrese numero decimal:"))
binario = ""
while numero> 0:
    resto = numero%2
    numero = numero//2
    binario = str(resto) + binario

print("resultado = "+binario)