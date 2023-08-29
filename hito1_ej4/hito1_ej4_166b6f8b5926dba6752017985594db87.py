#Conversión de Decimal a Binario
def resuladoBinario(numero):
    binario=''
    while numero // 2 != 0:
        binario = str(numero % 2) + binario
        numero = numero // 2
    return str(numero) + binario

numeroConvertir=int(input("ingrese el valor a convertir a Binario\n"))
n=(resuladoBinario(numeroConvertir))
#print(f"resultado {n}")
print("resultado=",n)

