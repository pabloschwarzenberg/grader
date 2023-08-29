#Ordenar tres números
n1=input("Ingrese un número entero: ")
n2=input("Ingrese un segundo número entero: ")
n3=input("Ingrese un tercer número entero: ")
if n1 >= n2 >= n3:
  print(n3,",",n2,",",n1)
if n1 >= n3 >= n2:
  print(n2, ",",n3, ",",n1)
if n2 >= n1 >= n3:
  print(n3,",",n1,",",n2)
if n2 >= n3 >= n1:
  print(n1,",",n3,",",n2)
if n3 >= n2 >= n1:
  print(n1,",",n2,",",n3)
if n3 >= n1 >= n2:
  print(n2,",",n1,",",n3)
 