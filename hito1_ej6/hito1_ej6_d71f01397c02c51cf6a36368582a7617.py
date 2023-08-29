#Ordenar tres números
a=int(input("Escriba un numero: "))
b=int(input("Escriba un segundo numero: "))
c=int(input("Escriba un tercer numero: "))

if a<=c<=b:
    print(a,",",c,",",b)
elif b<=a<=c:  
    print(b,",",a,",",c)
elif c<=b<=a:
    print (c,",",b,",",a)
elif b<=c<=a:
    print(b,",",c,",",a)
elif a<=b<=c:
    print(a,",",b,",",c)
elif c<=a<=b:
    print(c,",",a,",",b)  