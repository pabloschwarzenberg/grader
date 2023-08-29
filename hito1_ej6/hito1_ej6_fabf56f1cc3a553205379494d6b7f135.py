a=int(input("Ingrese el valor de a: "))
b=int(input("Ingrese el valor de b: "))
c=int(input("Ingrese el valor de c: "))

if a<b<c:
  print(a,",",b,",",c)
if b<a<c:
  print(b,",",a,",",c)
if c<a<b:
  print(c,",",a,",",b)
if a<c<b:
  print(a,",",c,",",b)
if b<c<a:
  print(b,",",c,",",a)
if c<b<a:
  print(c,",",b,",",a)
if a==c<b:
  print(a,",",c,",",b)
if a==c==b:
  print(a,",",c,",",b)
if b<a==c:
  print(b,",",a,",",c)