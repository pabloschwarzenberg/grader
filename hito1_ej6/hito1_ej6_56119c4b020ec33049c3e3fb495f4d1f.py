#Ordenar tres números
lista = []
for num in range(3):
  numero = int(input("Ingrese un numero: "))
  lista.append(numero)
lista.sort()
print(lista)