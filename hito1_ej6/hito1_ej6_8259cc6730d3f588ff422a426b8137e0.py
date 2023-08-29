#Ordenar tres números
a=int(input("Número 1: "))
b=int(input("Número 2: "))
c=int(input("Número 3: "))
if a<b<c:
    print(a,",",b,",",c)
elif a<c<b:
    print(a,",",c,",",b)
elif b<a<c:
    print(b,",",a,",",c)
elif b<c<a:
    print(b,",",c,",",a)
elif c<a<b:
    print(c,",",a,",",b)
elif c<b<a:
    print(c,",",b,",",a)
elif a<c and a==b:
    print(a,",",b,",",c)
elif a<b and a==c:
    print(a,",",c,",",b)
elif b<a and b==c:
    print(c,",",b,",",a)
elif b<c and b==a:
    print(b,",",a,",",c)
elif c<b and c==a:
    print(c,",",a,",",b)
elif c<a and c==b:
    print(c,",",b,",",a)
elif a==b==c:
    print(c,",",b,",",a)