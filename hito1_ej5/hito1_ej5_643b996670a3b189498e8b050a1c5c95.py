#Cálculo del dígito verificador de un rut
a=(input())

if int(a)>=10000000:
    a0=(a[0])
    a1=(a[1])
    a2=(a[2])
    a3=(a[3])
    a4=(a[4])
    a5=(a[5])
    a6=(a[6])
    a7=(a[7])
    b1=int(a7)*2
    b2=int(a6)*3
    b3=int(a5)*4
    b4=int(a4)*5
    b5=int(a3)*6
    b6=int(a2)*7
    b7=int(a1)*2
    b8=int(a0)*3
    b9=b1+b2+b3+b4+b5+b6+b7+b8
    b10=b9%11
    b11=11-b10
    if b11==11:
        print("dv=",0)
    elif b11==10:
        print("dv=K")
    elif b11<10:
        print("dv=",b11)
if int(a)<10000000:
    a0=(a[0])
    a1=(a[1])
    a2=(a[2])
    a3=(a[3])
    a4=(a[4])
    a5=(a[5])
    a6=(a[6])
    c1=int(a6)*2
    c2=int(a5)*3
    c3=int(a4)*4
    c4=int(a3)*5
    c5=int(a2)*6
    c6=int(a1)*7
    c7=int(a0)*2
    c9=c1+c2+c3+c4+c5+c6+c7
    c10=c9%11
    c11=11-c10
    if c11==11:
        print("dv=",0)
    elif c11==10:
        print("dv=K")
    elif c11<10:
        print("dv=",c11)