#Ordenar tres números
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))

if a==b==c:
    print(a,",",b,",",c)
else:
    if a<b<c:
       print(a,",",b,",",c)

if c<b<a:
    print(c,",",b,",",a)

if b<c<a:
    print(b,",",c,",",a)

if b<a<c:
    print(b,",",a,",",c)

if a<c<b:
    print(a,",",c,",",b)

if c<a<b:
    print(c,",",a,",",b)

if a==b<c:
    print(a,",",b,",",c)

if a<b==c:
    print(a,",",b,",",c)

if b<a==c:
    print(b,",",a,",",c)

if a==c<b:
    print(a,",",c,",",b)

if b==c<a:
    print(b,",",c,",",a)

if c==b<a:
    print(c,",",b,",",a)

if c==a<b:
    print(c,",",a,",",b)

if c<a==b:
    print(c,",",a,",",b)
     