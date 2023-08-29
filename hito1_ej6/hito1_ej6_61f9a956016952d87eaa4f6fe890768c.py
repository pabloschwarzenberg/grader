a=int(input("ingrese el primer número:"))
b=int(input("ingrese el segundo número:"))
c=int(input("ingrese el tercer número:"))

if a<b and a<c and b<c:
    print(a,",",b,",",c)
elif a<c and a<b and c<b:
    print(a,",",c,",",b)

if a<b and a<c and b==c:
    print(a,",",b,",",c)
elif a<c and a<b and c==b:
    print(a,",",c,",",b)

elif b<a and b<c and a<c:
    print(b,",",a,",",c)
elif b<c and b<a and c<a:
    print(b,",",c,",",a)
elif b<a and b<c and a==c:
    print(b,",",a,",",c)
elif b<c and b<a and c==a:
    print(b,",",c,",",a)

elif c<a and c<b and a<b:
    print(c,",",a,",",b)
elif c<b and c<a and b<a:
    print(c,",",b,",",a)
elif c<a and c<b and a==b:
    print(c,",",a,",",b)
elif c<b and c<a and b==a:
    print(c,",",b,",",a)