#Ordenar tres números
n1=int(input("Ingrese valor n1: "))
n2=int(input("Ingrese valor n2: "))
n3=int(input("Ingrese valor n3: "))
if n1>n2:
  if n2>n3:
    print("{},{},{}".format(n3,n2,n1))
  else:
    if n1>n3:
      print("{},{},{}".format(n2,n3,n1))
    else:
      print("{},{},{}".format(n2,n1,n3))
else:
  if n1>n3:
    print("{},{},{}".format(n3,n1,n2))
  else:
    if n2>n3:
      print("{},{},{}".format(n1,n3,n2))
    else:
      print("{},{},{}".format(n1,n2,n3))
