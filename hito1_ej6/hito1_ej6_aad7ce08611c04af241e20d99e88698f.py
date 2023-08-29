#Ordenar tres número
a = int(input("ingrese un numero: "))
b = int(input("ingrese otro número: "))
c = int(input("ingrese un tercer numero: "))
if a<=b and a<=c and b<=c:
  print(a, ",", b,",",  c)
if a<=c and a<=b and c<=b:
  print(a,",", c,",",  b)
if b<=c and b<=a and c<=a:
  print(b,",", c,",",  a)
if b<=c and b<=a and a<=c:
  print(b,",", a,",",  c)
if c<=a and c<=b and a<=b:
  print(c,",", a,",", b)
if c<=a and c<=b and b<=a:
  print(c,",", b,",", a)
