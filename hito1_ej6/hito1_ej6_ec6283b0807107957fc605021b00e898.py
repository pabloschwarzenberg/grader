#Ordenar tres números
print("Ingrese 3 digitos los cuales se le entregaran ordenados de menor a mayor")
n1 = int(input("Ingrese su primer digito: "))
n2 = int(input("Ingrese su segundo digito: "))
n3 = int(input("Ingrese su tercer digito: "))
if n1 < n2 < n3:
  print(n1,",",n2,",",n3)
if n1 < n3 < n2:
  print(n1,",",n3,",",n2)
if n2 < n3 < n1:
  print(n2,",",n3,",",n1)
if n2 < n1 < n3:
  print(n2,",",n1,",",n3)
if n3 < n2 < n1:
  print(n3,",",n2,",",n1)
if n3 < n1 < n2:
  print(n3,",",n1,",",n2)
if n3 > n1 > n2:
  print(n3,",",n1,",",n2)
if n1 == n2 == n3:
  print(n3,",",n1,",",n2)
if n1 == n2 > n3:
  print(n3,",",n1,",",n2)
if n1 == n2 < n3:
  print(n1,",",n2,",",n3)
if n2 == n3 > n1:
  print(n1,",",n2,",",n3)
if n2 == n3 < n1:
  print(n2,",",n3,",",n1)
if n3 == n1 > n2:
  print(n2,",",n3,",",n1)
if n3 == n1 < n2:
  print(n3,",",n1,",",n2)