#Ordenar tres números
lista = []
for i in range (0,3):
  n = int(input("ingrese 3 numeros: "))
  lista.append(n)
  for i in range(0,len(lista)):
    for j in range(0,len(lista)):
        if (lista[i]<lista[j]):
            burbuja = lista[i]
            lista[i] = lista[j]
            lista[j] = burbuja

print(lista)

    
  
  