#Ordenar tres números
a = int(input("Ingrese primer número: "))
b = int(input("Ingrese segundo número: "))
c = int(input("Ingrese tercer número: "))

if a <= b <= c:
    print(a,",",b, ",",c)
if a <= c <= b:
    print(a,",",c, ",",b)
if b <= a <= c:
    print(b,",",a,",",c)
if b <= c <= a:
    print(b,",",c,",",a)
if c <= a <= b:
    print(c,",", a,",",b)
if c <= b <= a:
    print(c,",",b,",",a)