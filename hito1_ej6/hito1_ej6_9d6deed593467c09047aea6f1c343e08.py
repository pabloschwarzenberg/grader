#Ordenar tres números
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
n3 = int(input("Ingresa el tercer número: "))

if n1 <= n2 and n1 <= n3:
  print(n1, end=", ")
  if n2 <= n3:
    print(n2, end=", ")
    print(n3)
  else:
    print(n3, end=", ")
    print(n2)
elif n2 <= n1 and n2 <= n3:
  print(n2, end=", ")
  if n1 <= n3:
    print(n1, end=", ")
    print(n3)
  else:
    print(n3, end=", ")
    print(n1)
else:
  print(n3, end=", ")
  if n1 <= n2:
    print(n1, end=", ")
    print(n2)
  else:
    print(n2, end=", ")
    print(n1)