#Ordenar tres números
a=input("Inserte el primer número:")

b=input("Inserte el segundo número:")

c=input("Inserte el tercer número:")

if a<=b and b<=c :
    
    print(a,",",b,",",c)

elif b<=a and a<=c :

    print(b,",",a,",",c)

elif c<=a and a<=b :

    print(c,",",a,",",b)

elif a<=c and c<=b :

    print(a,",",c,",",b)

elif b<=c and c<=a :

    print(b,",",c,",",a)

elif c<=b and b<=a :

    print(c,",",b,",",a)     