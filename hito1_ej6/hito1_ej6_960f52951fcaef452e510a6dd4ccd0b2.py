#Ordenar tres números
a = eval(input("ingrese un numero: "))
b = eval(input("ingrese un numero: "))
c = eval(input("ingrese un numero: "))
if (a > b and b > c): 
    print("",c , ",",b , ",",a)
else:
    if(a > c and c > b):
        print("",b,",",c,",",a)
    else:
        if(b > a and a > c):
            print("",c,",",a,",",b)
        else:
            if(b > c and c > a):
                print("",a,",",c,",",b)
            else:
                if(c > a and a > b):
                    print("",b,",",a,",",c)
                else:
                    if(c > b and b > a):
                        print("",a ,",",b ,",",c)
                    else:
                        if(a == b and a > c):
                            print("",c,",",b,",",a)
                        else:
                            if(a == b and a < c):
                                print("",b,",",a,",",c)
                            else:
                                if(a == c and a > b):
                                    print("",b ,",",c,",",a)
                                else:
                                    if(a == c and a < b):
                                        print("",c,",",a,",",b)
                                    else:
                                        if(b == c and b < a):
                                            print("",c,",",b,",",a)
                                        else:
                                            if(b == c and b > a):
                                                print("",a,",",c,",",b)
                                            else:
                                                (b == c and b == a)
                                                print("",a,",",b,",",c)
                                                                            