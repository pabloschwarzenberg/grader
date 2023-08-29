#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if((a<b<c) or (a==b<c) or (a<b==c)):
    print(a,",",b,",",c)
if((a<c<b) or (a==c<b) or (a<c==b)):
    print(a,",",c,",",b)
if((b<a<c) or (b<a==c)):
    print(b,",",a,",",c)
if((b<c<a) or (b==c<a)):
    print(b,",",c,",",a)
if((c<b<a) or (c<b==a)):
    print(c,",",b,",",a)
if(c<a<b):
      print(c,",",a,",",b)
