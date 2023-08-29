#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
# a<b<c a<c<b b<c<a b<a<c c<a<b c<b<a
if(a<=b<=c):
    print(a,",",b,",",c)
else:
    if(a<=c<=b):
        print(a,",",c,",",b)
    else:
        if(b<=c<=a):
            print(b,",",c,",",a)
        else:
            if(b<=a<=c):
                print(b,",",a,",",c)
            else:
                if(c<=a<=b):
                    print(c,",",a,",",b)
                else:
                    print(c,",",b,",",a)