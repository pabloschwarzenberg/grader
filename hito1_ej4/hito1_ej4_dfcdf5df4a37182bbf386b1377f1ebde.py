#Conversión de Decimal a Binario
def nbinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario
    
b=int(input())
print("resultado=", nbinario(b))
