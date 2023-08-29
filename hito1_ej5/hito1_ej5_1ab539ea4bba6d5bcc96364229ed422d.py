rut = str(input("Ingrese su rut sin digito verificador: "))
if len(rut)==8:
    n=(int(rut[0])*3)+(int(rut[1])*2)+(int(rut[2])*7)+(int(rut[3])*6)+(int(rut[4])*5)+(int(rut[5])*4)+(int(rut[6])*3)+(int(rut[7])*2)
    m=n%11
    if m!=1 and m!=0:
        d=11-m
        print("dv=",d)
    elif m==0:
        print("dv=",0)
    else:
        print("dv=k")
elif len(rut)==7:
    n=(int(rut[0])*2)+(int(rut[1])*7)+(int(rut[2])*6)+(int(rut[3])*5)+(int(rut[4])*4)+(int(rut[5])*3)+(int(rut[6])*2)
    m=n%11
    if m!=1 and m!=0:
        d=11-m
        print("dv=",d)
    elif m==0:
        print("dv=",0)
    else:
        print("dv:k")

