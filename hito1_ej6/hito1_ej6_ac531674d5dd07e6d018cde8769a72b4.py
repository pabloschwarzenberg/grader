a=int(input("ingrese su primer numero"))
b=int(input("ingrese su segundo numero"))
c=int(input("ingrese su tercer numero"))
if a<b<c:
  print(a,",",b,",",c)
elif a<c<b:
  print(a,",",c,",",b)
elif b<c<a:
  print(b,",",c,",",a)
elif b<a<c:
  print(b,",",a,",",c)
elif c<a<b:
  print(c,",",a,",",b)
elif c<b<a:
  print(c,",",b,",",a)
elif a==b:
  if a<c:
    print(a,",",b,",",c)
  else:
    print(c,",",b,",",a)
elif a==c:
  if a<b:
    print(a,",",c,",",b)
  else:
    print(b,",",c,",",a)
elif b==c:
  if b<a:
    print(b,",",c,",",a)
  else:
    print(a,",",c,",",b)