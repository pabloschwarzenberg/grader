a=int(input())
b=int(input())
c=int(input())
if a > b > c:
    print(c,",",b,",",a)
if a > c > b:
    print(b,",",c,",",a)
if b > a > c:
    print(c,",",a,",",b)
if b > c > a:
    print(a,",",c,",",b)
if c > a > b:
    print(b,",",a,",",c)
if c > b > a:
    print(a,",",b,",",c)
if a==b>c:
    print(c,",",b,",",a)
if a==b<c:
    print(b,",",a,",",c)
if b==c>a:
    print(a,",",b,",",c)
if b==c<a:
    print(c,",",b,",",a)
if a==c>b:
    print(b,",",c,",",a)
if a==c<b:
    print(c,",",a,",",b)