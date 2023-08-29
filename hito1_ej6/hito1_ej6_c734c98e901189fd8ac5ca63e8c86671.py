#Entrada
#Iterador
k = 0
lista = []
#Entrada
while k < 3:
  n = int(input("Ingrese numero: "))
  lista.append(n)
  k += 1
#Ordenamiento
i = 0
j = 0
while i < len(lista):
  while j < len(lista):
    if lista[i] < lista[j]:
      t = lista[i]
      lista[i] = lista[j]
      lista[j] = t
    j+=1
  i+=1
  j=0
#Salida
print(lista[0],",",lista[1],",",lista[2])


