#Ordenar tres números
a=int(input("num 1:"))
b=int(input("num 2:"))
c=int(input("num 3:"))

if a<=b<=c:
    print(a,",",b,",",c)

if a<=c<=b:
    print(a,",",c,",",b)

if b<=a<=c:
    print(b,",",a,",",c)

if b<=c<=a:
    print(b,",",c,",",a)

if c<=a<=b:
    print(c,",",a,",",b)

if c<=b<=a:
    print(c,",",b,",",a)