#Ordenar tres números

print("Ingrese tres numeros, ninguno puede ser igual")
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))

if a <= b and a < c:
    print (a,",",b,",",c)
else:
    if a <= c and a < b:
        print (a,",",c,",",b)
    else:
        if b <= c and b < a:
            print(b,",",c,",",a)
        else:
            if a < b and a < c and b < c:
                print (a,",",b,",",c)
            else:
                if a < b and a < c and c < b:
                    print(a,",",c,",",b)
                else:
                    if b < a and b < c and a < c:
                        print(b,",",a,",",c)
                    else:
                        if b < a and b < c and c < a:
                            print(b,",",c,",",a)
                        else:
                            if c < a and c < b and b < a:
                                print(c,",",b,",",c)
                            else:
                                if c < a and c < b and a < b:
                                    print(c,",",a,",",b)