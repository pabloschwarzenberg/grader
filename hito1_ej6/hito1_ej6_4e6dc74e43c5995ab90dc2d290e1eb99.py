#Ordenar tres números

a = input("Ingrese numero: ")
b = input("Ingrese numero: ")
c = input("Ingrese numero: ")
try:
  a = int(a)
  b = int(b)
  c = int(c)
# ordenamiento
  if a > b  and a > c:
    if c > b:
      print(b, ",", c, ",", a)
    else:
      print(c, ",", b, ",", a)
  elif b > a and b > c:
      if a > c:
        print(c, ",", a, ",", b)
      else:
        print(a, ",", c, ",", b)
  elif c > a and c > b:
    if a > b:
      print(b, ",", a, ",", c)  
    else:
      print(a, ",", b, ",", c)
except ValueError:
  print("Eso no es un numero.")