a=int(input())
b=int(input())
c=int(input())
if a!=b and b!=c and a!=c:
    if a>b>c:
        print(c,",",b,",",a)
    if a>c>b:
        print(b,",",c,",",a)
    if b>a>c:
        print(c,",",a,",",b)
    if b>c>a:
        print(a,",",c,",",b)
    if c>a>b:
        print(b,",",a,",",c)
    if c>b>a:
        print(a,",",b,",",c)
else:
    if a==b:
        if a>c:
            print(c,",",a,",",a)
        if c>a:
            print(a,",",a,",",c)
    if a==c:
        if a>b:
            print(b,",",a,",",a)
        if b>a:
            print(a,",",a,",",b)
    
    if c==b:
        if c>b:
            print(b,",",c,",",c)
        if b>c:
            print(c,",",c,",",b)
