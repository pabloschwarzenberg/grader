#Cálculo del dígito verificador de un rut
rut=eval(input('Ingrese su rut sin el dígito verificador: '))

if 1000000<=rut<=99999999:
    if 1000000<=rut<=9999999:
        d7=rut%10
        rut=rut//10
        d6=rut%10
        rut=rut//10
        d5=rut%10
        rut=rut//10
        d4=rut%10
        rut=rut//10
        d3=rut%10
        rut=rut//10
        d2=rut%10
        rut=rut//10
        d1=rut%10
        suma=d7*2+d6*3+d5*4+d4*5+d3*6+d2*7+d1*2
        resto=suma%11
        dv=11-resto
        if dv==11:
            print('dv=0')
        if dv==10:
            print('dv=K.')
        if 1<=dv<=9:
            print('dv=',dv)
    if 10000000<=rut<=99999999:
        d8=rut%10
        rut=rut//10
        d7=rut%10
        rut=rut//10
        d6=rut%10
        rut=rut//10
        d5=rut%10
        rut=rut//10
        d4=rut%10
        rut=rut//10
        d3=rut%10
        rut=rut//10
        d2=rut%10
        rut=rut//10
        d1=rut%10
        suma=d8*2+d7*3+d6*4+d5*5+d4*6+d3*7+d2*2+d1*3
        resto=suma%11
        dv=11-resto
        if dv==11:
            print('dv=0')
        if dv==10:
            print('dv=K')
        if 1<=dv<=9:
            print('dv=',dv)
else:
    print('ERROR,Digite un rut valido.')