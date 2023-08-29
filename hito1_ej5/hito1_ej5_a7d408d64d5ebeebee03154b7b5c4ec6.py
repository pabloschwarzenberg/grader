rut=str(input("Ingresar rut: "))
if len(rut)==8:
    a=int(rut[-1])*2
    b=int(rut[-2])*3
    c=int(rut[-3])*4
    d=int(rut[-4])*5
    e=int(rut[-5])*6
    f=int(rut[-6])*7
    g=int(rut[-7])*2
    h=int(rut[-8])*3
    n=a+b+c+d+e+f+g+h
    r=n%11
    p=11-r
    if p==11:
        print("dv=0")
    elif p==10:
        print("dv=k")
    else:
        print("dv=",q)
elif len(rut)==7:
    a=int(rut[-1])*2
    b=int(rut[-2])*3
    c=int(rut[-3])*4
    d=int(rut[-4])*5
    e=int(rut[-5])*6
    f=int(rut[-6])*7
    g=int(rut[-7])*2
    n=a+b+c+d+e+f+g
    r=n%11
    p=11-r
    if p==11:
        print("dv=0")
    elif p==10:
        print("dv=k")
    else:
        print("dv=",p)