#Cálculo del dígito verificador de un rut
s=input("ingrese rut= ")

if len(s)==8:
    s1=s[-1]
    s2=s[-2]
    s3=s[-3]
    s4=s[-4]
    s5=s[-5]
    s6=s[-6]
    s7=s[-7]
    s8=s[-8]

    sa=int(s1)*2
    sb=int(s2)*3
    sc=int(s3)*4
    sd=int(s4)*5
    se=int(s5)*6
    sf=int(s6)*7
    sg=int(s7)*2
    sh=int(s8)*3

    suma=sa+sb+sc+sd+se+sf+sg+sh
    divisor=suma%11
    dv=11-divisor
    if dv==10:
        print("dv=k")
    elif dv==11:
        print("dv=0")
    else:
        print("dv=",dv)

if len(s)==7:
    s1=s[-1]
    s2=s[-2]
    s3=s[-3]
    s4=s[-4]
    s5=s[-5]
    s6=s[-6]
    s7=s[-7]

    sa=int(s1)*2
    sb=int(s2)*3
    sc=int(s3)*4
    sd=int(s4)*5
    se=int(s5)*6
    sf=int(s6)*7
    sg=int(s7)*2

    suma1=sa+sb+sc+sd+se+sf+sg
    divisor1=suma1%11
    dv1=11-divisor1
    if dv1==10:
        print("dv=k")
    elif dv1==11:
        print("dv=0")
    else:
        print("dv=",dv1)