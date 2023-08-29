#Ordenar tres números
a=int(input("Ingrese a: "))
b=int(input("Ingrese b: "))
c=int(input("Ingrese c: "))
if a>=b>=c:
    print(c,",",b,",",a)
if a>=c>b:
    print(b,",",c,",",a)
if b>=c>=a:
    print(a,",",c,",",b)
if b>a>c:
    print(c,",",a,",",b)
if c>a>=b:
    print(b,",",a,",",c)
if c>b>a:
    print(a,",",b,",",c)
