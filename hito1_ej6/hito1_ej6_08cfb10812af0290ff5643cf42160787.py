#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if c<b<a:
    print("{0},{1},{2}".format(c,b,a))
else:
    if c<a<b:
        print("{0},{1},{2}".format(c,a,b))
    else:
        if a<c<b:
            print("{0},{1},{2}".format(a,c,b))
        else:
                if a<b<c:
                    print("{0},{1},{2}".format(a,b,c))
                else:
                        if b<a<c:
                            print("{0},{1},{2}".format(b,a,c))
                        else:
                            print("{0},{1},{2}".format(b,c,a))