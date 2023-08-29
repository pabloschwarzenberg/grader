#Ordenar tres números
a=int(input("ingrese un numero_1:"))
b=int(input("ingrse un numero_2:"))
c=int(input("ingrese un numero_3:"))

if  a<=b<=c:
    print(a,",",b,",",c)
    
if  a<=c<=b:
    print(a,",",c,",",b)
    
if  c<=a<=b:
        print(c,",",a,",",b)
    
if  c<=b<=a:
    print(c,",",b,",",a)
    
if  b<=c<=a:
    print(b,",",c,",",a)
    
if  b<=a<=c:
    print(b,",",a,",",c)
    
       