rut=input('Ingrese los numero del rut: ')
if len(rut)==7:

    list_rut=[]
    for i in rut:
        list_rut.append(int(i))

    num1=list_rut[0]*2
    num2=list_rut[1]*7
    num3=list_rut[2]*6
    num4=list_rut[3]*5
    num5=list_rut[4]*4
    num6=list_rut[5]*3
    num7=list_rut[6]*2
    

    dv_1=(num1+num2+num3+num4+num5+num6+num7)
    dv=(dv_1-(dv_1//11)*11)

    if dv==11:
        print('dv=0')
    elif dv==10:
        print('dv=K')
    else:
        print('dv=',dv)

elif len(rut)==8:

    list_rut=[]
    for i in rut:
        list_rut.append(int(i))

    num1=list_rut[0]*3
    num2=list_rut[1]*2
    num3=list_rut[2]*7
    num4=list_rut[3]*6
    num5=list_rut[4]*5
    num6=list_rut[5]*4
    num7=list_rut[6]*3
    num8=list_rut[7]*2

    dv_1=(num1+num2+num3+num4+num5+num6+num7+num8)
    dv=(dv_1-(dv_1//11)*11)

    if dv==11:
        print('dv=0')
    elif dv==10:
        print('dv=K')
    else:
        print('dv=',dv)
else:
    print('No es la cantidad de numeros que se requiere.')