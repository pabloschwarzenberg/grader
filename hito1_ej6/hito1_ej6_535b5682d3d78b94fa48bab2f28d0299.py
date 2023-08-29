a=int(input("Ingresar primer numero: "))
b=int(input("Ingresar segundo numero: "))
c=int(input("Ingresar tercer numero: "))
if a > b and a < c:
    print(b,",",a,",",c)
if b > a and b < c:
    print(a,",",b,",",c)
if c > a and c < b:
    print(a,",",c,",",b)
if a == b and b==c:
    print(a,",",b,",",c)
if a == b:
    if c > a:
        print(a,",",b,",",c)
    else:
        print(c,",",b,",",a)
if a==c:
    if b > a:
        print(a,",",c,",",b)
    else:
        print(b,",",a,",",c)
if b == c:
    if a > b:
        print(b,",",c,",",a)
    else:
        print(a,",",b,",",c)
