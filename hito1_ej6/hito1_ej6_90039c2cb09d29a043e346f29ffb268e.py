#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())

if a<=b<=c:
    print(a,",",b,",",c)
elif a<=c<=b:
    print(a,",",c,",",b)
elif c<=a<=b:
    print(c,",",a,",",b)
elif c<=b<=a:
    print(c,",",b,",",a)
elif b<=c<=a:
    print(b,",",c,",",a)
else :
    print(b,",",a,",",c)
