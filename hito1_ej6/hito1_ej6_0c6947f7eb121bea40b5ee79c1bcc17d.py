#Ordenar tres números
a = int(input("ingrese un numero"))
b = int(input("ingrese un numero"))
c = int(input("ingrese un numero"))

if a<b and b<c:
  print(a,",",b,",",c)
elif b<a and a<c:
  print(b,",",a,",",c)
elif b>c and c>a:
  print(a,",",c,",",b)
elif a>c and c>b:
  print(b,",",c,",",a)
elif c<b and b<a:
  print(c,",",b,",",a)
elif c<a and a<b:
  print(c,",",a,",",b)
elif b==a and c<a:
  print(c,",",b,",",a)
elif c==b and b<a:
  print(c,",",b,",",a)
elif c==a and a<b:
  print(c,",",a,",",b)