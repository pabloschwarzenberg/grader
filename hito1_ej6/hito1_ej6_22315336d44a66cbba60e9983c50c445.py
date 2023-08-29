a=input(("numero a: "))
b=input(("numero b: "))
c=input(("numero c: "))

if a<=b<=c:
    print(a,",", b,",", c)
elif b<=c<=a:
    print(b, ",",c,",", a)
elif c<=b<=a:
    print(c,",", b, ",",a)
elif a<=c<=b:
    print(a,",", c,",", b)
elif c<=a<=b:
    print(c, ",",a, ",",b)
elif b<=a<=c:
    print(b,",", a,",", c)





if a==b==c:
    print(a,",", b,",", c)
elif b==c==a:
    print(b,",", c,",", a)
elif c==b==a:
    print(c,",", b, ",",a)
elif a==c==b:
    print(a, ",",c, ",",b)
elif c==a==b:
    print(c, ",",a, ",",b)
elif b==a==c:
    print(b,",", a, ",",c)
