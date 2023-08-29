#Conversión de Decimal a Binario
def binari(d):
    binario = ''
    while d // 2 != 0:
        binario = str(d % 2) + binario
        d = d // 2
    return str(d) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print("Resultado=",binari(numero))