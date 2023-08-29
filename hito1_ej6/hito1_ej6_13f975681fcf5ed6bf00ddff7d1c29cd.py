#Ordenar tres números   
a=input("ingresar numero 1:")
b=input("ingresar numero 2:")
c=input("ingresar numero3:")
if(a>b>c):
   print (c,",",b,",",a)
if(a<b<c):
    print (a,",",b,",",c)
if(c<a<b):
    print (c,",",a,",",b)
if(b<c<a):
    print (b,",",a,",",c)
if(b<a<c):
    print (b,",",a,",",c)
if(a<c<b):
    print(a,",",c,",",b)
if(a==c<b):
    print (c,",",a,",",b)
if(a==c>b):
    print (b,",",c,",",a)
if(b==a<c):
    print(b,",",a,",",c)
if(b==a>c):
    print(c,",",b,",",a)
