#Ordenar tres números
a=int(input())
b=int(input())
c=int(input())
if a>=b and b>=c:
    print("{0},{1},{2}".format(c,b,a))
else:
    if a>=c and c>=b:
        print("{0},{1},{2}".format(b,c,a))
    else:
        if b>=a and a>=c:
            print("{0},{1},{2}".format(c,a,b))
        else:
            if b>=c and c>=a:
                print("{0},{1},{2}".format(a,c,b))
            else:
                if c>=b and b>=a:
                    print("{0},{1},{2}".format(a,b,c))
                else:
                    if c>=a and a>=b:
                        print("{0},{1},{2}".format(b,a,c))
                    else:
                        print("error")
