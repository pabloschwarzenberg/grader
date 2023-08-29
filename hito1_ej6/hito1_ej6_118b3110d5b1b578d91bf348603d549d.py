#Ordenar tres números
a = int(input("Ingrese un número entero:"))
b = int(input("Ingrese un segundo número entero:"))
c = int(input("Ingrese un tercer número entero:"))
if a==b and a==c and b==c:
  print(a,",",b,",",c)
if a==b and a<c:
  print(a,",",b,",",c)
if a==b and a>c:
  print(c,",",a,",",b)
if a==c and a<b:
  print(a,",",c,",",b)
if a==c and a>b:
  print(b,",",a,",",c)
if b==c and b<a:
  print(b,",",c,",",a)
if b==c and b>a:
  print(a,",",b,",",c)
if a>b and b>c:
  print(c,",",b,",",a)
if a>c and c>b:
  print(b,",",c,",",a)
if b>a and a>c:
  print(c,",",a,",",b)
if b>c and c>a:
  print(a,",",c,",",b)
if c>a and a>b:
  print(b,",",a,",",c)
if c>b and b>a:
  print(a,",",b,",",c)