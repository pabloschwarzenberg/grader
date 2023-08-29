#Ordenar tres números
a=int(input("Escriba el primer numero: "))
b=int(input("Escriba el segundo numero: "))
c=int(input("Escriba el tercer numero: "))
if(a <= b <= c):
    print(a,",",b,",",c)
elif (a <= c <= b):
    print(a, ",",c,",",b)
elif (b <= a <= c):
    print(b,",",a,",",c)
elif (b <= c <= a):
    print(b,",",c,",",a)
elif (c <= a <= b):
    print(c,",",a,",",b)
elif (c <= b <= a):
    print(c,",",b,",",a)