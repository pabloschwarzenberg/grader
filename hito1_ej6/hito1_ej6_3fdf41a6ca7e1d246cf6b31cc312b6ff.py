#Ordenar tres números
a=int(input("ingrese n1"))
b=int(input("inrgese n2"))
c=int(input("ingrese n3"))

if a<=b and a<=c :
  print(a,",")
  if b<=c:
    print(b,",")
    print(c)
  else:
      print(c,",")
      print(b)
if b<=a and b<=c :
  print(b,",")
  if a<=c:
    print(a,",")
    print(c)
  else:
      print(c,",")
      print(a)
if c<=b and c<=a :
  print(c,",")
  if b<=a:
    print(b,",")
    print(a)
  else:
      print(a)
      print(b)
      