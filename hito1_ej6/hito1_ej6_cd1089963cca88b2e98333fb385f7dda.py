#Ordenar tres números
print("calculo de cual numero es mayor")
a=int(input("ingrese el valor de un numero:"))
b=int(input("ingrese el valor de otro numero:"))
c=int(input("ingrese el valor de otro numero:"))
if a>=b and b>=c:
    print(c,",",b,",",a)
elif a<=c and c<=b:
    print(a,",",c,",",b)
elif b<=a and a<=c:
    print(b,",",a,",",c)
elif b<=c and c<=a:
    print(b,",",c,",",a)    
elif a>=c and a<=b:
    print(c,",",a,",",b)
else:
    c<=b and b<a
    print(a,",",b,",",c)