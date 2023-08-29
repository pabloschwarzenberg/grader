a=input()
b=input()
c=input()

if a<b and b<c:
    print(a,",", b ,",",c)
else:
    if b<a and a<c:
        print(b,",",a,",",c)
    else:
        if c<a and a<b:
            print(c,",",a,",",b)
        else:
            if c<b and b<a:
                print(c,",",b,",",a)
            else:
                if a<c and c<b:
                    print(a,",",c,",",b)
                else:
                    if b<c and c<a:
                        print(b,",",c,",",a)
                    else:
                        if a==b and b<c:
                            print(a,",",b,",",c)
                        else:
                            if a==c and c<b:
                                print(a,",",c,",",b)
                            else:
                                if b==c and c<a:
                                    print(b,",",c,",",a)
                                else:
                                    if a==b and b>c:
                                        print(c,",",b,",",a)
                                    else:
                                        if a==c and c>b:
                                            print(b,",",a,",",c)
                                        else:
                                            if b==c and c>a:
                                                print(a,",",b,",",c)

                                
                                    

                                                
                                          
