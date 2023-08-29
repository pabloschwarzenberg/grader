#Conversión de Decimal a Binario
def binario(decimal):
    numeroBinario = ''
    while decimal // 2 != 0:
        numeroBinario = str(decimal % 2) + numeroBinario
        decimal = decimal // 2
    return str(decimal) + numeroBinario

x = int(input("Ingresa el numero que quieres convertir --> "))
print("resultado =",binario(x))