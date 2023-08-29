a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a<b<c:
  print(a,",", b,",", c)
elif a==b==c:
  print(a,",", b,",", c)
elif a<b and a<c and b==c:
  print(a,",", b,",", c)
if a<c<b:
  print(a,",", c,",", b)
if b<a<c:
  print(b,",", a,",", c)
elif b<a and b<c and a==c:
  print(b,",", a,",", c)
elif b>a and b>c and a==c:
  print(a,",", c,",", b)
if b<c<a:
  print(b,",", c,",", a)
if c<b<a:
  print(c,",", b,",", a)
elif c<a and c<b and a==b:
  print(c,",", b,",", a)
if c<a<b:
  print(c,",", a,",", b)