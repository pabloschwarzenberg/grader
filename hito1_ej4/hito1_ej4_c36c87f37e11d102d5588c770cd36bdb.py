#Conversión de Decimal a binario
def bin(decimal):
    resultado = numero
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    print("resultado")
    
numero = int(input('Introduce el número para convertir a binario: '))
print("resultado =",bin(numero))