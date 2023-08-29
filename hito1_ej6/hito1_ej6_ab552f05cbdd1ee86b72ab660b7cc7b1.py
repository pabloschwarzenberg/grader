#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a>=b and b>=c:
    print(c,",",b,",",a)
elif b>=a and a>=c:
    print(c,",",a,",",b)
elif a>=c and c>=b:
    print(b,",",c,",",a)
elif b>=c and c>=a:
    print(a,",",c,",",b)
elif c>=a and a>=b:
    print(b,",",a,",",c)
elif c>=b and b>=a:
    print(a,",",b,",",c)