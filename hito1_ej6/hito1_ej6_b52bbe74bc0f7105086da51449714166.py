#Ordenar tres números
a=int(input("Primer numero"))
b=int(input("2"))
c=int(input("3"))
if a<=b and b<=c:
    print(a,",",b,",",c)
elif a<=b and c<=b:
    print(a,",",c,",",b)
elif b<=a and a<=c:
    print(b,",",a,",",c)
elif b<=c and c<=a:
    print(b,",",c,",",a)
elif c<=a and a<=b:
    print(c,",",a,",",b)
elif c<=b and b<=a:
    print(c,",",b,",",a)
elif a<=c and b<=a:
    print(b,",",a,",",c)
    
    