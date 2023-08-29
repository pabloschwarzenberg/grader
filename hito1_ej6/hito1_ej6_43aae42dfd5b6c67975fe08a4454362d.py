a=int(input("Ingrese un número: "))
b=int(input("Ingrese un número: "))
c=int(input("Ingrese un número: "))
if a<b<c:
    print(a,",",b,",",c)
if a<c<b:
    print(a,",",c,",",b)
if b<a<c:
    print(b,",",a,",",c)
if b<c<a:
    print(b,",",c,",",a)
if c<a<b:
    print(c,",",a,",",b)
if c<b<a:
    print(c,",",b,",",a)
if a==b<c:
    print(a,",",b,",",c)
if a==b==c:
    print(a,",",b,",",c)
if a<b==c:
    print(a,",",b,",",c)
if a>b==c:
    print(b,",",c,",",a)
if b<a==c:
    print(b,",",a,",",c)
if b>a==c:
    print(a,",",c,",",b)
if c<a==b:
    print(c,",",a,",",b)