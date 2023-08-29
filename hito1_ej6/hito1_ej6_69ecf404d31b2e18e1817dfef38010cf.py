#Ordenar tres números
a=(int(input("Ingresa tu primer numero")))
   
b=(int(input("Ingresa tu segundo numero")))
   
c=(int(input("Ingresa tu tercer numero")))

if a>b>c:
   print(c,",",b,",",a)
if b>a>c:
   print(c,",",a,",",b)
if c>a>b:
   print(b,",",a,",",c)
if a>c>b:
   print(b,",",c,",",a)
if b>c>a:
   print(a,",",c,",",b)
if c>b>a:
   print(a,",",b,",",c)
if b==a>c:
    print(c,",",a,",",b)
if c==a>b:
    print(b,",",a,",",c)
if b==c>a:
   print(a,",",c,",",b)
if a==b==c:
    print(a,",",b,",",c)
if a==b<c:
    print(a,",",b,",",c)
if a==c<b:
    print(a,",",c,",",b)
if c==b<a:
    print(c,",",b,",",a)
