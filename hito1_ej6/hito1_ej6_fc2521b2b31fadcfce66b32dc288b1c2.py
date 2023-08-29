#Ordenar tres números
a=input("escriba un numero (a):")
b=input("escriba un numero (b):")
c=input("escriba un numero (c):")
a=int(a)
b=int(b)
c=int(c)
if a>=b and b>=c:
    print(c,",",b,",",a)
elif a>=b and b<=c and a>=c:
    print(b,",",c,",",a)
elif c>=a and a>=b:
    print(b,",",a,",",c)
elif c>=a and a<=b and c>=b:
    print(a,",",b,",",c)
elif b>=a and a>=c:
    print(c,",",a,",",b)
elif b>=a and a<=c and b>=c:
    print(a,",",c,",",b)