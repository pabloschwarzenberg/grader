
a=int(input("Ingrese el primer numero :"))
b=int(input("Ingrese el segundo numero:"))
c=int(input("Ingrese el tercer numero:"))
if(a<=b<=c):
    print(a,",",b,",",c)
elif(a<=c<=b):
    print(a,",",c,",",b)
elif(b<=c<=a):
    print(b,",",c,",",a)
elif(b<=a<=c):
    print(b,",",a,",",c)
elif(c<=b<=a):
    print(c,",",b,",",a)
else:
    print(c,",",a,",",b)