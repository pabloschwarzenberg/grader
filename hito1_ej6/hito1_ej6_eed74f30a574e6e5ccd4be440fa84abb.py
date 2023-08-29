lista = []
for x in range(3):
  num = int(input("Escriba numeros enteros: "))
  lista.append(num)
menor = lista[0]
medio = lista[0]
mayor = lista[0]
for i in lista:
  if (i > mayor):
    mayor = i
for i in lista:
  if (i < menor):
    menor = i
for i in lista:
  if (i > menor) and (i < mayor):
    medio = i
resultado = [menor, medio, mayor]
print(resultado)