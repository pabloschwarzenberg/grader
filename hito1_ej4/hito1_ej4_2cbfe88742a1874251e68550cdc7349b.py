#Conversión de Decimal a Binario

numero = int(input("Ingrese Número decimal: "))
conversion = ""
while numero//2 !=0:
    
    residuo = numero%2
    conversion = conversion+str(residuo)
    numero = numero//2

if numero == 1:
    conversion = conversion + "1"   
    
conversion = conversion[:: - 1 ]    
print(conversion)