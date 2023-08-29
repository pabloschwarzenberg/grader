#Ordenar tres números
a=eval(input('Ingrese un número'))
b=eval(input('ingrese un número'))
c=eval(input('ingrese un número'))
if a>b and b>c and a>c:
        print(c,',',b,',',a)
else:
        if a>b and c>b and a>c:
                print(b,',',c,',',a)
        else:
                if b>a and a>c and b>c:
                        print(c,',',a,',',b)
                else:
                        if b>a and c>a and b>c:
                                print(a,',',c,',',b)
                        else:
                                if c>a and a>b and c>a:
                                        print(b,',',a,',',c)
                                else:
                                        if c>a and b>a and c>b:
                                                print(a,',',b,',',c)
                                        else:
                                                if a>b and b==c:
                                                        print(c,',',b,',',a)
                                                else:
                                                        if b>a and a==c:
                                                                print(c,',',a,',',b)
                                                        else:
                                                                if c>a and a==b:
                                                                        print(b,',',a,',',c)
                                                                else:
                                                                        if a>b and a==c:
                                                                                print(b,',',a,',',c)
                                                                        else:
                                                                                if b>a and b==c:
                                                                                        print(a,',',b,',',c)