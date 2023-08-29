#Ordenar tres números
a=int(input("primer numero:"))
b=int(input("segundo numero:"))
c=int(input("tercer numero:"))
if a>=b and b>=c:
    print(c,",",b,",",a)
else:
    if a>=b and c>=a:
        print(b,",",a,",",c)
    else:
        if a<=b and b<=c:
            print(a,",",b,",",c)
        else:
            if c>=a and c<=b :
                print(a,",",c,",",b)
            else:
                if c<=a and a<=b:
                    print(c,",",a,",",b)
                else:
                    if b<=c and c<=a:
                        print(b,",",c,",",a)