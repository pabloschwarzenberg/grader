#Cálculo del dígito verificador de un rut
a=input()
b=(a[::-1])
n=(len(b))
if n==8:
    b1=(b[:1])
    c=int(b1)*2
    b2=(b[1:2])
    d=int(b2)*3
    b3=(b[2:3])
    e=int(b3)*4
    b4=(b[3:4])
    f=int(b4)*5
    b5=(b[4:5])
    g=int(b5)*6
    b6=(b[5:6])
    h=int(b6)*7
    b7=(b[6:7])
    i=int(b7)*2
    b8=(b[7:])
    j=int(b8)*3
    suma=(c+d+e+f+g+h+i+j)
    r=int(round(suma//11,0))
    numero=abs(suma-(r*11))
    dv=11-numero
    if dv==11:
        print("dv=",0)
    if dv==10:
        print("dv=k")
    if dv<10:
        print("dv=",dv)
if n==7:
    b1=(b[:1])
    c=int(b1)*2
    b2=(b[1:2])
    d=int(b2)*3
    b3=(b[2:3])
    e=int(b3)*4
    b4=(b[3:4])
    f=int(b4)*5
    b5=(b[4:5])
    g=int(b5)*6
    b6=(b[5:6])
    h=int(b6)*7
    b7=(b[6:])
    i=int(b7)*2
    suma=(c+d+e+f+g+h+i)
    r=int(round(suma//11,0))   
    numero=abs(suma-(r*11))
    dv=11-numero
    if dv==11:
        print("dv=",0)
    if dv==10:
        print("dv=k")
    if dv<10:
        print("dv=",dv)