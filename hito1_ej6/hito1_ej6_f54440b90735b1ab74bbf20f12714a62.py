a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a >= b and b >= c:
  print("El numero de menor a mayor es: ", str(c) + ", ", str(b) + ", ", str(a))
elif a >= c and c >= b:
  print("El numero de menor a mayor es: ", str(b) + ", ", str(c) + ", ", str(a))
elif b >= a and a >= c:
  print("El numero de menor a mayor es: ", str(c) + ", ", str(a) + ", ", str(b))
elif b >= c and c >= a:
  print("El numero de menor a mayor es: ", str(a) + ", ", str(c) + ", ", str(b))
elif c >= a and a >= b:
  print("El numero de menor a mayor es: ", str(b) + ", ", str(a) + ", ", str(c))
elif c >= b and b >= a:
  print("El numero de menor a mayor es: ", str(a) + ", ", str(b) + ", ", str(c))
  