#Conversión de Decimal a Binario
numero = int(input("Ingrese Numero"))
codigoBinario = ""
while numero > 0:
    codigoBinario = codigoBinario + str(numero % 2)
    numero = int(numero / 2)

i = len(codigoBinario) - 1
codigoBinarioInvertido = ""
while i >= 0:
    codigoBinarioInvertido = codigoBinarioInvertido + codigoBinario[i]
    i -= 1
print("resultado="+codigoBinarioInvertido)