#Ordenar tres números
print("En este programa se ordenaran de menor a mayor tres numeros naturales a eleccion.")
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))
c=int(input("Ingrese el tercer numero: "))
if(a<=b<=c):
    print(a,",",b,",",c,".")
else:
    if(a<=c<=b):
        print(a,",",c,",",b,".")
    else:
        if(b<=a<=c):
            print(b,",",a,",",c,".")
        else:
            if(b<=c<=a):
                print(b,",",c,",",a,".")
            else:
                if(c<=a<=b):
                    print(c,",",a,",",b,".")
                else:
                    if(c<=b<=a):
                        print(c,",",b,",",a,".")