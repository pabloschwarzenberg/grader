x=int(input('ingrese un numero de hasta 4 digitos'))
if 1000<=x<=9999:
    U=x%10
    x=x//10
    D=x%10
    x=x//10
    C=x%10
    x=x//10
    M=x%10
    print('el resultado es:',str(M),'M','+',str(C),'C','+',str(D),'D','+',str(U),'U')
else:
    if 100<=x<=999:
        U=x%10
        x=x//10
        D=x%10
        x=x//10
        C=x%10
        print ('el resultado es:',str(C),'C','+',str(D),'D','+',str(U),'U')
    else:
        if 10<=x<=99:
            U=x%10
            x=x//10
            D=x%10
            print('el resultado es:',str(D),'D','+',str(U),'U')
        else:
            if 0<=x<=9:
                U=x
                print('el resultado es:',str(U),'U')
 