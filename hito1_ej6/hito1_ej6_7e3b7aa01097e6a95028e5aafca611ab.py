#Ordenar tres números
a=int(input(" a inserte un numero: "))
b=int(input(" b inserte un numero: "))
c=int(input(" c inserte un numero: "))

if a>b and a>c and b>c :
    print(c,",",b,",",a)
if a>b and a>c and b<c:
    print(b,",",c,",",a)
if b>a and b>c and a>c:
    print(c,",",a,",",b)
if b>a and b>c and a<c:
    print(a,",",c,",",b)
if c>a and c>b and a<b:
    print(a,",",b,",",c)
if c>a and c>b and a>b:
    print(b,",",a,",",c)
if a==b and b==c and c==a:
    print(c,"=",b,"=",a)
if b==a and c>a:
    print(a,",",b,",",c)
if c==b and a>b:
    print(c,",",b,",",a)
if a==c and b>a:
    print(a,",",c,",",b)
if b==a and c<a:
    print(c,",",b,",",a)
if c==b and a<b:
    print(a,",",b,",",c)
if a==c and b<a:
    print(b,",",c,",",a)