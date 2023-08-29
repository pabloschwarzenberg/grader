#Ordenar tres números
a= int(input("numero 1 "))
b= int(input("numero 2 "))
c= int(input("numero 3 "))
if a>b>c:
     print(c,",",b,",",a)
if b>a>c:
     print(c,",",a,",",b)
if c>a>b:
     print(b,",",a,",",c)
if c>b>a:
     print(a,",",b,",",c)
if a>c>b:
     print(b,",",c,",",a)
if b>c>a:
     print(a,",",c,",",b)
if a>=b>c:
     print(c,",",b,",",c)
if a>=c>b:
     print(b,",",c,",",a)
if b>=c>a:
     print(a,",",c,",",b)     