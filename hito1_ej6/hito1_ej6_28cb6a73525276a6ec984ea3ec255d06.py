#Ordenar tres números
a=int(input("valor 1:"))
b=int(input("valor 2:"))
c=int(input("valor 3:"))
if a<b and a<c and b<c:
    print(a,",",b,",",c)
else:
    if a<c and a<b and c<b:
        print(a,",",c,",",b)
    else:
            if b<c and b<a and c<a:
                print(b,",",c,",",a)
            else:
                   
                   if b<a and b<c and a<c:
                           print(b,",",a,",",c)
                   else:
                            if c<a and c<b and a<b:
                                print(c,",",a,",",b)
                            else:
                                    if c<b and c<a and b<a:
                                        print(c,",",b",",a)
                                    
if a==b and a<c:
    print(a,",",b,",",c)
else:
        if a==c and a<b:
            print(a,",",c,",",b)
        else:
            if b==c and b<a:
                print(b,",",c,",",a)
            else:
                if a==c and b<c:
                    print(b,",",a,",",c)
        
