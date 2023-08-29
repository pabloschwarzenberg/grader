#Ordenar tres númerosprint("Escriba tres números enteros, uno a la vez.")
a=int(input("Nº1: "))
b=int(input("Nº2: "))
c=int(input("Nº3: "))

if(a<=b<=c):
    print(a,",",b,",",c)
else:
    if(a<=c<=b):
        print(a,",",c,",",b)
    else:
        if(b<=c<=a):
            print(b,",",c,",",a)
        else:
            if(b<=a<=c):
                print(b,",",a,",",c)
            else:
                if(c<=a<=b):
                    print(c,",",a,",",b)
                else:
                    if(c<=b<=a):
                        print(c,",",b,",",a)