a = int(input("Ingrese un numero: "))
b = int(input("Ingrese un numero: "))
c = int(input("Ingrese un numero: "))

if c<=b<=a:
    print("el resultado es: ",c,",",b,",",a)
elif c<=a<=b:
    print("el resultado es: ",c,",",a,",",b)
elif a<=b<=c:
    print("el resultado es: ",a,",",b,",",c)
elif a<=c<=b:
    print("el resultado es: ",a,",",c,",",b)
elif b<=c<=a:
    print("el resultado es: ",b,",",c,",",a)
elif b<=a<=c:
    print("el resultado es: ",b,",",a,",",c)