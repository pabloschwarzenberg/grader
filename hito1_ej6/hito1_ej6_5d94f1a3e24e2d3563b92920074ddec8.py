#Ordenar tres números
a= int(input("Numero 1:"))
b=int(input("Numero 2:"))
c=int(input("Numero 3:"))

if a>b>c or a==b>c or a>b==c:
    x = print(c,',',b,',',a)
else:
    if c>b>a or c==b>a or c>b==a:
        print(a,',', b,',', c)
    else:
            if a>c>b or a==c>b or a>c==b:
                print(b,',',c,',',a)
            else:
                    if c>a>b or c==a>b or c>a==b:
                        print(b,',',a,',',c)
                    else:
                            if b>c>a or b==c>a or b>c==a:
                                print(a,',',c,',',b)
                            else:
                                    if b>a>c or b==a>c or b>a==c:
                                        print(c,',',a,',',b)
        

       

