#Conversión de Decimal a Binario
def binari(x):

    binario = ''

    while x // 2 != 0:

        binario = str(x % 2) + binario

        x = x // 2

    return str(x) + binario

 

n = int(input('ingrese el numero: '))

print("Resultado=",binari(n))     