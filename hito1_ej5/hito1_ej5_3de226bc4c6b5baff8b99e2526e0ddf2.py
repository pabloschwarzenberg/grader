#Cálculo del dígito verificador de un rut
rut=input()
if len(rut)==7:
    a=int(rut[0])*2+int(rut[1])*7+int(rut[2])*6+int(rut[3])*5+int(rut[4])*4+int(rut[5])*3+int(rut[6])*2
    print(a)
    b=(a//11)
    print(b)
    c=a-(11*b)
    print(c)
    d=11-c
    print(d)
    if d== 11:
        print("dv=0")
    if d== 10:
        print("dv=K")
    else:
        print("dv=",d)
if len(rut)==8:
    e=int(rut[0])*3+int(rut[1])*2+int(rut[2])*7+int(rut[3])*6+int(rut[4])*5+int(rut[5])*4+int(rut[6])*3+int(rut[7])*2
    print(e)
    f=(e//11)
    print(f)
    g=e-(11*f)
    print(g)
    h=11-g
    print(h)
    if h== 11:
        print("dv=0")
    if h== 10:
        print("dv=K")
    else:
        print("dv=",h)