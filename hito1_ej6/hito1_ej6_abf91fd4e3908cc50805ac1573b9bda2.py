#Ordenar tres números
a=int(input("ingresar numero A: "))
b=int(input("ingresar numero B: "))
c=int(input("ingresar numero C: "))

if a <= b <= c:
    print(a,",",b,",",c)

if a <= c <= b:
    print(a,",",c,",",b)

if b <= a <= c:
    print(b,",",a,",",c)

if b <= c <= a:
    print(b,",",c,",",a)

if c <= a <= b:
    print(c,",",a,",",b)

if c <= b <= a:
    print(c,",",b,",",a)
