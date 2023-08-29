#Ordenar tres números
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
if a <= b and a <= c:
 if b <= c:
  print (a,",",b,",",c)
if c <= b:
 print (a,",",c,",",b)
if b <= a and b <= c:
 if a <= c:
  print (b,",",a,",",c)
if c <= a:
 print (b,",",c,",",a)
if c <= b and c <= a:
 if b <= a:
  print (c,",",b,",",a)
if a <= b:
 print (c,",",a,",",b)