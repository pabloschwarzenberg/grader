#Conversión de Decimal a Binario
def ahoraBinario(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

resultado = int(input("Introduce el decimal que quieras a binario >>> "))

print("resultado = ", ahoraBinario(resultado))