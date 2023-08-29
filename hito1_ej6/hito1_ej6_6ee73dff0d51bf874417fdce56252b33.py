#Ordenar tres números
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if(a<=b):
    if(b<=c):
        print(a,",",b,",",c)
    if(b>=c):
        if(a<=c):
            print(a,",",c,",",b)
        else:
           print(c,",",a,",",b)

if(b<a):
    if(a<=c):
        print(b,",",a,",",c)
    if(a>=c):
        if(b<=c):
            print(b,",",c,",",a)
        else:
           print(c,",",b,",",a)
