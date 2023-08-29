#Descomponer un número
numero = int(input('ingrese un numero de hasta 4 digitos'))
a = ['U', 'D', 'C', 'M']
numero = str(numero)
listanumeros = list(numero)
digitos = len(numero)
listanumeros1 = listanumeros.reverse()
lista = []
b = 0
for f in range(digitos):
    lista.append(listanumeros[f]+a[f])
lista.reverse()
b='+'.join(lista)
print(b)