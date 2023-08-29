a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))

if a<b<c:
    print (a,",",b,",",c)
if a>b>c:
    print (c,",",b,",",a)
if a>b and a>c and b<c:
    print (b,",",c,",",a)
if a>b and a<c and b<c:
    print (b,",",a,",",c)
if a<b and a>c and b>c:
    print (c,",",a,",",b)
if a<b and a<c and b>c:
    print (a,",",c,",",b)
if a==c and b>c:
    print (a,",",a,",",b)
if a==c and b<c:
    print (b,",",a,",",a)
if a==b==c:
    print(a,",",a,",",a,",")
