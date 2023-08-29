#Conversión de Decimal a Binario

numero = int(input("Ingrese un numero entero: "))

numeroBinario = bin(numero)
#type(numeroBinario)
#print(type(numeroBinario))
#print(numeroBinario)
print("resultado=" + format(numero, '0b'))