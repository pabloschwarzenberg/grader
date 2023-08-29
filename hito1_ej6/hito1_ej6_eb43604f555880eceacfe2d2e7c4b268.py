#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a!=b!=c:
  print(sorted([a,b,c]))
elif a==b:
  if a<c:
    print(a,",",b,",",c)
  else:
    print(c,",",b,",",a)
elif b==c:
  if b<a:
    print(b,",",c,",",a)
  else:
    print(a,",",b,",",c)
elif c==a:
  if a<b:
    print(a,",",c,",",b)
  else:
    print(b,",",c,",",a)
else:
  print(a,",",b,",",c)