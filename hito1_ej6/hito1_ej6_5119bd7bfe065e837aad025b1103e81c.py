import math
a=int(input("a:"))

b=int(input("b:"))

c=int(input("c:"))

if a<b and b<c:
 print(a,",",b,",",c)
 
elif c<b and b<a:
 print(c,",",b,",",a)

elif b<c and c<a:
 print(b,",",c,",",a)

elif a<c and c<b:
 print(a,",",c,",",b)

elif b<a and a<c:
 print(b,",",a,",",c)

elif c<a and a<b:
 print(c,",",a,",",b)
 
elif a==b and b<c:
 print(a,",",b,",",c)
 print(b,",",a,",",c)

elif b==c and a<b:
 print(a,",",b,",",c)
 print(a,",",c,",",b)

elif a==c and b>a:
 print(a,",",c,",",b)
 print(c,",",a,",",b)

elif a==c and b<a:
 print(b,",",a,",",c)
 print(b,",",c,",",a)

elif a==b==c:
 print(a,",",b,",",c)
 print(a,",",c,",",b)
 print(b,",",a,",",c)
 print(b,",",c,",",a)
 print(c,",",a,",",b)
 print(c,",",b,",",a)