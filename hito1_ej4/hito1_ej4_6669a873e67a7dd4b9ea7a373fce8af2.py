#Conversión de Decimal a Binario
numero = int(input("ingrese un numero:"))
binario = ""
while numero > 0:
    residuo = numero%2
    numero = numero // 2
    binario = str(residuo)+binario
    
print("resultado=",binario)