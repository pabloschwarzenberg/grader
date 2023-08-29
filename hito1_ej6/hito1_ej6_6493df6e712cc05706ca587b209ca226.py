#Ordenar tres números
n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el segundo numero: "))
n3 = int(input("Ingrese es tercer numero: "))

if n1 >= n2 >= n3:
  print(n3,end=",")
  print(n2,end=",")
  print(n1,end=",")
elif n2 >= n3 >= n1:
  print(n1,end=",")
  print(n3,end=",")
  print(n2,end=",")
elif n3 >= n1 >= n2:
  print(n2,end=",")
  print(n1,end=",")
  print(n3,end=",")
elif n3 >= n2 >= n1:
  print(n1,end=",")
  print(n2,end=",")
  print(n3,end=",")
elif n1 >= n3 >= n2:
  print(n2,end=",")
  print(n3,end=",")
  print(n1,end=",")
elif n1 == n2 == n3:
  print(n1,end=",")
  print(n2,end=",")
  print(n3,end=",")