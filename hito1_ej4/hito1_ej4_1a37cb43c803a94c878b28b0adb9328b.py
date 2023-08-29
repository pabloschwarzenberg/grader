#Conversión de Decimal a Binario
numero = int(input("Ingresa un número decimal: "))
binario = ""  

while numero > 0:
    resto = numero % 2  
    binario = str(resto) + binario 
    numero = numero//2
    
print("resultado =", binario)        