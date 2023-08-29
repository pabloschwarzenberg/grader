#Ordenar tres números
n1 = int(input("ingrese un numero entero: "))
n2 = int(input("ingrese un segundo numero entero: "))
n3 = int(input("ingrese un tercer numero entero: "))
if n1>= n2 >= n3:
  print(n3,",", n2,",", n1, sep =(""))
if n1 >= n3 >= n2:
  print(n2,",", n3,",", n1, sep =(""))
if n2 >= n1 >= n3:
  print(n3,",", n1,",", n2, sep =(""))
if n2 >= n3 >= n1:
  print(n1,",", n3,",", n2, sep =(""))
if n3 >= n1 >=n2:
  print(n2,",", n1,",", n3, sep =(""))