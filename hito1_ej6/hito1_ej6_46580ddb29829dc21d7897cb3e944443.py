#Ordenar tres números
a = int(input("Ingrese un numero entero"))
b = int(input("Ingrese un numero entero"))
c = int(input("Ingrese un numero entero"))

if a <= b <= c:
  print(a,",", b ,",",c)
if a <= c <= b:
  print(a, "," , c, "," ,b)
if b <= a <= c:
  print(b,",",a,",",c)
if b <= c <= a:
  print(b,",",c,",",a)
if c <= b <= a:
  print(c,",",b,",",a)
if c <= a <= b:
  print(c,",",a,",",b)