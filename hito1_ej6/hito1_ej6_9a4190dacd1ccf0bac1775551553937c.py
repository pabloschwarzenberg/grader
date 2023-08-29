a=input("Ingrese el primer numero: ")
b=input("Ingrese el segundo numero: ")
c=input("Ingrese el tercer numero: ")



if a<b<c or b==c>a:
    print(a,",",b,",",c)
if a<b and b>c and a<c:
    print(a,",",c,",",b)
if a>b and b<c and c>a or a==c>b:
    print(b,",",a,",",c)
if a>b and b<c and c<a:
    print(b,",",c,",",a)
if a<b and b>c and a>c or b==a>c:
    print(c,",",a,",",b)
if a>b and b>c:
    print(c,",",b,",",a)
    
if a==b<c:
    print(b,",",a,",",c)
if a==c<b:
    print(c,",",a,",",b)
if b==c<a:
    print(c,",",b,",",a)