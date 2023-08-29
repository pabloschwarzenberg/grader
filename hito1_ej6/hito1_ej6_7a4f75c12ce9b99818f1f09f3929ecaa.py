#Ordenar tres números
print("Ingrese 3 números enteros:")
n1 = int(input()) 
n2 = int(input())
n3 = int(input())
if n1 >= n2 >= n3:
  print(n3,",", n2,",", n1, sep =(""))
if n1 >= n3 >= n2:
  print(n2,",", n3,",", n1, sep =(""))
if n2 >= n1 >= n3:
  print(n3,",", n1,",", n2, sep =(""))
if n2 >= n3 >= n1:
  print(n1,",", n3,",", n2, sep =(""))
if n3 >= n1 >= n2:
  print(n2,",", n1,",", n3, sep =(""))
if n3 >= n2 >= n1:
  print(n1,",", n2,",", n3, sep =(""))