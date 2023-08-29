#Factores Primos
a=int(input("ingrese el valor de un numero:"))
b=int(input("ingrese el valor de otro numero:"))
c=int(input("ingrese el valor de otro numero:"))
if a>b and b>c:
    print("El menor es",a,",""el sesgundo es",b,",""el numero mayor es",c)
elif a<c and c<b:
    print("El menor es",a,",""el sesgundo es",c,",""el numero mayor es",b)
elif b<a and a<c:
    print("El menor es",b,",""el sesgundo es",a,",""el numero mayor es",c)
elif b<c and c<a:
    print("El menor es",b,",""el sesgundo es",c,",""el numero mayor es",a)    
elif a>c and a<b:
    print("El menor es",c,",""el sesgundo es",a,",""el numero mayor es",b)
else:
    c<b and b<a
    print("El menor es",c,",""el sesgundo es",b,",""el numero mayor es",a)
