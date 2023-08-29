# Descomponer un número

numero = input()
numero = list(numero)
lista = ['M', 'C', 'D', 'U']
i = 0
x = -1
while i < len(numero):
    numero[x] = str(numero[x]) + str(lista[x])
    i += 1
    x -= 1

print(*numero, sep='+')



