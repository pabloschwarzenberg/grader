#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a>=b>=c:
   print(c,",",b,",",c)
if a>=c>=b:
   print(b,",",c,",",a)
if b>=a>=c:
   print(c,",",a,",",b)
if b>=c>=a:
   print(a,",",c,",",b)
if c>=a>=b:
   print(b,",",a,",",c)
if c>=b>=a:
   print(a,",",b,",",c)