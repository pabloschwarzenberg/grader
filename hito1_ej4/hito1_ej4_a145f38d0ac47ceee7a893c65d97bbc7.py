#Conversión de Decimal a Binario
def numabinario(numero):

    binario = ""
    while numero // 2 != 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return str(numero) + binario


final = int(input("Introduce el numero que sera transformado "))
print("resultado =",(numabinario(final)))
