#Ordenar tres números
a=int(input("Ingrese número: "))
b=int(input("Ingrese número: "))
c=int(input("Ingrese número: "))

if(a<=b<=c):
    print(a,",",b,",",c)
else:
    if(a<=c<=b):
        print(a,",",c,",",b)
    else:
        if(c<=b<=a):
            print(c,",",b,",",a)
        else:
            if(c<=a<=b):
                print(c,",",a,",",b)
            else:
                if(b<=a<=c):
                    print(b,",",a,",",c)
                else:
                    if(b<=c<=a):
                        print(b,",",c,",",a)

   