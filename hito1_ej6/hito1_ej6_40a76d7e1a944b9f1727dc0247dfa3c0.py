#Ordenar tres números
a=int(input("escriba un numero: "))
b=int(input("escriba un segundo numero: "))
c=int(input("escriba un tercer numero: "))

if( a<=b<=c ):
    print("el orden es",a,",",b,",",c)
elif(a<=c<=b):
    print("el orden es",a,",",c,",",b)
elif(b<=a<=c):
    print("el orden es",b,",",a,",",c)
elif(b<=c<=a):
    print("el orden es",b,",",c,",",a)
elif(c<=a<=b):
    print("el orden es",c,",",a,",",b)
elif(c<=b<=a):
    print("el orden es",c,",",b,",",a)
else:
    print("no se puede calcular")