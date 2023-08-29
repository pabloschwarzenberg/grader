a=int(input("ingresar a: "))
b=int(input("ingresar b: "))
c=int(input("ingresar c: "))

if a <= b <= c:
    print(a,",",b,",",c)
elif b <= a <= c:
    print(b,",",a,",",c)
elif b <= c <= a:
    print(b,",",c,",",a)
elif c <= b <= a:
    print(c,",",b,",",a)
elif c <= a <= b:
    print(c,",",a,",",b)
else:
    print(a,",",b,",",c)
