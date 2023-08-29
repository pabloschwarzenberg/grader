#Conversión de Decimal a Binario
#ENTRADA

def binarizar(decimal):
    binario = ""
    
#PROCESAMIENTO
    
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

#SALIDA

numero = int(input('Introduce el digito que deseas convertir a binario: '))

print("resultado = ", binarizar(numero))     