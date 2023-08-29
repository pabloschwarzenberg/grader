#Ordenar tres números
import math
a = eval(input("Valor A:"))
b = eval(input("Valor B:"))
c = eval(input("Valor C:"))

if a<b<c:
    print(a,",",b,",",c)
elif c<b<a:
    print(c,",",b,",",a)
elif b<c<a:
    print(b,",",c,",",a)
elif b<a<c:
    print(b,",",a,",",c)
elif c<a<b:
    print(c,",",a,",",b)
elif a<c<b:
    print(a,",",c,",",b)
elif a==b>c:
    print(c,",",a,",",b)
elif a==b<c:
    print(a,",",b,",",c)
elif b==c>a:
    print(a,",",b,",",c)
elif b==c<a:
    print(b,",",c,",",a)
elif a==c>b:
    print(b,",",c,",",a)
elif a==c<b:
    print(a,",",c,",",b)
else:
    print("Vuelva a ingresar números")
