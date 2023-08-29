#Ordenar tres números
a = int(input("Ingrese primer numero"))
b = int(input("Ingrese segundo numero"))
c  = int(input("Ingrese tercer numero"))

if a > b and a < c and c > b:
    print(b,",",a,",",c)
if c > b and b > a and a < c:
    print(a,",",b,",",c)
if a > b and b > c and c < a:
    print(c,",",b,",",a)
if a > c and c > b and b < a:
    print(b,",",c,",",a)
if b > a and a > c and c < b:
    print(c,",",a,",",b)
if b > c and c < a and a < b:
    print(a,",",c,",",b)
if (a == b) != c:
    x = a
    x = b
    if x > c:
        print(c,",",b,",",a)
    if x < c:
        print(a,",",b,",",c)
if (b==c) != a:
    i = b
    i = c
    if i > a:
        print(a,",",c,",",b)
    if i < a:
        print(c,",",b,",",a)
if (a==c) != b:
    e = a
    e = c
    if e > b:
        print(b,",",c,",",a)
    if e < b:
        print(a,",",c,",",b)
if (a == b == c):
    print(a,",",c,",",b)