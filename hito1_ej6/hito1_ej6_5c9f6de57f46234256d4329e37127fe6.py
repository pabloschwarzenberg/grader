#Ordenar tres números
a=int(input("Ingresa número: "))
b=int(input("Ingresa número: "))
c=int(input("Ingresa número: "))
if c<=a and c<=b:
    if a<=b:
        print(c,",",a,",",b)
    if b<=a:
        print(c,",",b,",",a)
elif a<=b and a<=c:
    if b<=c:
        print(a,",",b,",",c)
    if c<=b:
        print(a,",",c,",",b)
elif b<=a and b<=c:
    if a<=c:
        print(b,",",a,",",c)
    if c<=a:
        print(b,",",c,",",a)
 