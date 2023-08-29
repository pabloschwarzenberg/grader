#inicio
n1 = int(input("Ingrese primer Número >>>"))
n2 = int(input("Ingrese segundo número >>>"))
n3 = int(input("ingrese tercer número >>>"))

#Desarrollo
if (n1 > n2 and n2 > n3):
      print([n3, n2, n1])
if (n1 > n2 and n1 < n3):
      print([n2, n1, n3])
if (n1 < n2 and n1 < n3):
      print([n1, n2, n3])
if (n1 < n2 and n1 > n3):
      print([n1, n3, n2])
if (n1 > n2 and n1 == n3):
      print([n2, n1, n3])
if (n1 < n2 and n1 == n3):
      print([n3, n1, n2])
if (n1 == n2 and n1 > n3):
      print([n3, n2, n1])
if (n1 == n2 and n1 < n3):
      print([n1, n2, n3])
if (n1 == n2 and n1 == n3):
      print([n1, n2, n3])