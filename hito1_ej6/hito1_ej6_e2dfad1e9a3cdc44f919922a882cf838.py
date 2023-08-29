a=int(input('ingrese numero'))
b=int(input('ingrese numero'))
c=int(input('ingrese numero'))
if a<b and a<c and b<c:
    print ('el orden es: ',a,',',b,',',c)
else:
    print ('el orden es: ',a,',',c,',',b)
    if b<a and b<c and a<c:
        print ('el orden es: ',b,',',a,',',c)
    else:
        print ('el orden es: ',b,',',c,',',a)
        if c<a and c<b and a<b:
            print ('el orden es: ',c,',',a,',',b)
        else:
                print ('el orden es: ',a,',',b,',',a)

