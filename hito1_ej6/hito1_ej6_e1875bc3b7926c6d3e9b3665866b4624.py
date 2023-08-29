#Ordenar tres números
a=input()
b=input()
c=input()

if c<=b<=a:
   print(c,",",b,",",a)
if b<=c<=a:
   print(b,",",c,",",a)
if c<=a<=b:
   print(c,",",a,",",b)
if a<=c<=b:
   print(a,",",c,",",b)
if a<=b<=c:
   print(a,",",b,",",c)
if b<=a<=c:
   print(b,",",a,",",c)
