#Ordenar tres números

a=int(input("Ingresa el primer numero entero:"))
x=int(input("Ingresa el segundo numero entero:"))
c=int(input("Ingresa el tercer numero entero:"))


if(a<=x<=c):
    print(a,",",x,",",c)
elif(a<=c<=x):
    print(a,",",c,",",x)
elif(x<=c<=a):
    print(x,",",c,",",a)
elif(x<=a<=c):
     print(x,",",a,",",c)
elif(c<=x<=a):
     print(c,",",x,",",a)
else:
    print(c,",",a,",",x)
