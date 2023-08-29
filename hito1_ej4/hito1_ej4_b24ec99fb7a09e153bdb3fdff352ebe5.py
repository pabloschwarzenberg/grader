#Conversión de Decimal a Binario
numero = int(input("Ingrese Numero Decimal:"))
resto = ""

while numero//2!=0:
    resto = str(numero%2)+resto
    numero = numero//2
    binario = str(numero)+resto

print("Resultado =",binario)
    
