#Ordenar tres números
a=int(input("Ingrese a:"))
b=int(input("Ingrese b:"))
c=int(input("Ingrese c:"))

if a<=b<=c:
   print(a,",",b,",",c)
if b<=c<=a:
   print(b,",",c,",",a)
if c<=a<=b:
   print(c,",",a,",",b)
if a<=c<=b:
   print(a,",",c,",",b)
if c<=b<=a:
   print(c,",",b,",",a)
if b<=a<=c:
   print(b,",",a,",",c)