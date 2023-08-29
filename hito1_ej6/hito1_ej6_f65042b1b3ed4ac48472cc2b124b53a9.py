#Ordenar tres números
a=int(input("Numero a"))
b=int(input("Numero b"))
c=int(input("Numero c"))

if a<=b<=c:
  print(a,",",b,",",c)
if a<=c<=b:
  print(a,",",c,",",b)
if b<=a<=c:
  print(b,",",a,",",c)
if b<=c<=a:
  print(b,",",c,",",a)
if c<=a<=b:
  print(c,",",a,",",b)
if c<=b<=a:
  print(c,",",b,",",a)