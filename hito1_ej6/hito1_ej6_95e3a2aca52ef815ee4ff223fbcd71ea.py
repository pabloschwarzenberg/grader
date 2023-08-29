#Ordenar tres números
a=int(input("ingrese el primer número: "))
b=int(input("ingrese el segundo número: "))
c=int(input("ingrese el tercer número: "))

if a<b<c:
    print(a, ",", b, ",", c)
elif a<c<b:
    print(a, ",", c, ",", b)
elif b<a<c:
    print(b, ",", a, ",", c)
elif b<c<a:
    print(b, ",", c, ",", a)
elif c<a<b:
    print(c, ",", a, ",", b)
elif c<b<a:
    print(c, ",", b, ",", a)
elif a==b and b==c:
    print(a, ",", b, ",", c)
elif a==b and a>c:
    print(c, ",", b, ",", a)
elif a==b and a<c:
    print(a, ",", b, ",", c)
elif a==c and a>b:
    print(b, ",", a, ",", c)
elif a==c and a<b:
    print(a, ",", c, ",", b)
elif b==c and c>a:
    print(a, ",", b, ",", c)
elif b==c and c<a:
    print(c, ",", b, ",", a)