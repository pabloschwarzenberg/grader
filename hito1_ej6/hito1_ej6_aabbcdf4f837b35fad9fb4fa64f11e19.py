def ordenarNumeros(n1,n2,n3):
  lista = [n1,n2,n3]
  n = len(lista)
  for i in range(n-1):
    for j in range(n-i-1):
      if lista[j] > lista[j+1]:
        lista[j+1],lista[j]=lista[j],lista[j+1]
  return lista

print('Introduce tres números: ')

num1 = int(input())
num2 = int(input())
num3 = int(input())

orden = ordenarNumeros(num1, num2, num3)

print("Aquí tienes los 3 números ordenados de menor a mayor:%i %i %i"+ str(orden))
