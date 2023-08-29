#Ordenar tres números
a = int(input("Ingrese primer valor:"))
b = int(input("Ingrese segundo valor:"))
c = int(input("Ingrese tercer valor:"))

if a<b<c:
    print(a,",",b,",",c)
else:
    if c<b<a:
        print(c,",",b,",",a)
    else:
        if b<c<a:
            print(b,",",c,",",a)

        else:
            if b<a<c:
                print(b,",",a,",",c)
            else:
                if c<a<b:
                    print(c,",",a,",",b)
                else:
                    if a<b and b==c:
                        print(a,",",b,",",c)
                    else:
                        if a>b and b==c:
                            print(b,",",c,",",a)
                        else:
                            if b>a and a==c:
                                print(a,",",c,",",b)
                            else:
                                if b<a and a==c:
                                    print(b,",",a,",",c)
                                else:
                                    if c>a and a==b:
                                        print(a,",",b,",",c)
                                    else:
                                        if c<a and a==b:
                                            print(c,",",a,",",b)
                                        else:
                                            if a==b==c:
                                                print(a,",",c,",",b)
                                            else:
                                                if a<c<b:
                                                    print(c,",",a,",",b)
                                                else:
                                                    print("Syntax Error")
                                                   
