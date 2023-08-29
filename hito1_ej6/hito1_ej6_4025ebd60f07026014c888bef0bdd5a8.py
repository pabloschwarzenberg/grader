#Ordenar tres números
a = int(input("ingresar valor de a:"))
b = int(input("ingresar valor de b:"))
c = int(input("ingresar valor de c:"))


if  a < b < c:
    print("El orden es",a,",",b,",",c)
elif a < c < b:
    print("El orden es",a,",",c,",",b)

elif b < c < a:
    print("El orden es",b,",",c,",",a)
elif b < a <c:
    print("El orden es",b,",",a,",",c)
elif c < a < b:
    print("El orden es",c,",",a,",",b)
elif  c < b < a:
    print("El orden es",c,",",b,",",a)
elif a < b == c:
    print("El orden es",a,",",b,",",c)
elif b < a == c:
    print("El orden es",b,",",a,",",c)
elif c < a == b:
    print("El orden es",c,",",a,",",b)
elif b == c < a:
    print("El orden es",b,",",c,",",a)
elif a == c < b: 
    print("El orden es",a,",",c,",",b)
else:
    if b == a < c:
        print("El orden es",b,",",a,",",c)