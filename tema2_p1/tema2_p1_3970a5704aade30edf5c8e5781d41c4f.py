n1 = int(input("escriba un numero: "))
n2 = int(input("escriba un numero mayor o igual al primero: "))
if n2 < n1:
  print("ingrese un numero mayor o igual al primero")
else:
  for i in range(n1,n2+1):
    if i % 2 == 0:
      print("el numero es par",i)
    else:
      print("el numero es impar",i)