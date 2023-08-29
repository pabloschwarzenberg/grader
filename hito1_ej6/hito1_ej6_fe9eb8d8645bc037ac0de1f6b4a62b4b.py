#Ordenar tres números
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
if a<b<c:
  print(a,",",b,",",c)
elif a<c<b:
  print(a,",",c,",",b)
elif c<a<b:
  print(c,",",a,",",b)
elif b<a<c:
  print(b,",",a,",",c)
elif b<c<a:
   print(b,",",c,",",a)
elif c<b<a:
  print(c,",",b,",",a)
elif b<a and a==c:
  print (b,",",a,",",c)