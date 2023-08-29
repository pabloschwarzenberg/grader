#Ordenar tres números
a=input()
b=input()
c=input()
if a<b and b<c:
    print(a+","+b+","+c)
if c<a and b<c:
    print(b+","+c+","+a)
if a<c and c<b:
    print(a+","+c+","+b)
if a<b and c<a:
    print(c+","+a+","+b)
if b<a and a<c:
    print(b+","+a+","+c)
if c<b and b<a:
    print(c+","+b+","+a)
if c==a and c>b:
    print(b+","+c+","+a)
if a==b and a>c:
    print(c+","+b+","+a)
if b==c and a>b:
    print(c+","+b+","+a)
if c==a and c<b:
    print(a+","+c+","+b)
if a==b and a<c:
    print(a+","+b+","+c)
if b==c and a<b:
    print(a+","+b+","+c)






