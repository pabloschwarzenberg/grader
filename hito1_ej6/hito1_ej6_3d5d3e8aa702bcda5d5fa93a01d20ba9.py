#Ordenar tres números
a=int(input("ingrese a: "))
b=int(input("ingrese b: "))
c=int(input("ingrece c: "))

if a>=b>=c:
    print(c,",",b,",",a)
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
