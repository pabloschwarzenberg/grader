#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a<b:
   if a<c and b<c:
   print(a,",",b,",",c)
   else:
   print(c,",",a,",",b)
else:
   if b<c:
      if c<a:
      print(b,",",c,",",a)
      else:
      print(b,",",c,",",a)
   else:
   print(c,",",b,",",a)
   elif c<a and b>c