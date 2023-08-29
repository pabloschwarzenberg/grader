#Conversión de Decimal a Binario
def binario(decimal):
    nbinario = ''
    while decimal // 2 != 0:
        nbinario = str(decimal % 2) + nbinario
        decimal = decimal // 2
    return str(decimal) + nbinario

numero = int(input("ingrese sus datos:"))
print("resultado=",binario(numero))