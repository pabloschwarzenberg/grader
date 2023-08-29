#Descomponer un número
N=input()
largo=int((len(N)))
if largo==1:
    a=N[0]
    print("{0}U".format(a))
else:
    if largo==2:
        a=N[0]
        b=N[1]
        print("{0}D+{1}U".format(a,b))
    else:
        if largo==3:
            a=N[0]
            b=N[1]
            c=N[2]
            print("{0}C+{1}D+{2}U".format(a,b,c))
        else:
            a=N[0]
            b=N[1]
            c=N[2]
            d=N[3]
            print("{0}M+{1}C+{2}D+{3}U".format(a,b,c,d))      