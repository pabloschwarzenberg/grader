#Conversión de Decimal a Binario
numDec = int(input('Introduce el número a convertir a binario: '))
binario = ""
while numDec > 0:  
    
    numero = numDec % 2  
    numDec = numDec // 2 
    binario = str(numero) + binario  
print("resultado =",binario)