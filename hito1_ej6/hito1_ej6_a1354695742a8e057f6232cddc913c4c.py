a=int(input("ingrese el primer numero: "))
b=int(input("ingrese el segundo numero: "))
c=int(input("ingrese el tercer numero: "))
if a<=b<=c:
  print(a,",",b,",",c)
if b<=a<=c:
  print(b,",",a,",",c)
if c<=b<=a:
  print(c,",",b,",",a)
if b<=c<=a:
  print( b,",",c,",",a)
if a<=c<=b:
  print(a,",",c,",",b)
if c<=a<=b:
  print(c,",",a,",",b)
