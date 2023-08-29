#Ordenar tres números
a=int(input("ingrese primer numero"))
b=int(input("ingrese segundo numero"))
c=int(input("ingrese tercer numero"))

if a==b and b==c:
    print(a,",",b,",",c)
elif a==b and b<c:
    print(a,",",b,",",c)
elif a==b and b>c:
    print (c,",",a,",",b)
elif a==c and a<b:
    print(a,",",c,",",b)
elif a==c and a>b:
    print(b,",",a,",",c)
elif b==c and b<a:
    print(b,",",c,",",a)
elif b==c and b>a:
    print(a,",",b,",",c)
elif (a<b) and (b<c) and (a<c):
    print(a,",",b,",",c)
elif (a<c) and (c<b)and (a<b):
    print(a,",",c,",",b)
elif (b<a) and (a<c) and (b<c):
    print(b,",",a,",",c)
elif (b<c) and (c<a) and (b<a):
    print(b,",",c,",",a)
elif(c<b) and (b<a) and (c<a):
    print(c,",",b,",",a)
elif(c<a) and (a<b) and (c<b):
    print(c,",",a,",",b)
