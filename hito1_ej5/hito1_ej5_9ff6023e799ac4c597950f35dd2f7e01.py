#Cálculo del dígito verificador de un rut
rut1=int(input())
if 10000000<=(rut1)<=99999999:
    rut=str(rut1)
    a=((int(rut[0])*3)+(int(rut[1])*2)+(int(rut[2])*7)+(int(rut[3])*6)+(int(rut[4])*5)+(int(rut[5])*4)+(int(rut[6])*3)+(int(rut[7])*2))
    b=a%11
    c=11-b
    if c==10:
        print("dv=k")
    elif c==11:
        print("dv=0")
    else:
        print("dv="+str(c))
elif 1000000<=rut1<=9999999:
    rut=str(rut1)
    a=((int(rut[0])*2)+(int(rut[1])*7)+(int(rut[2])*6)+(int(rut[3])*5)+(int(rut[4])*4)+(int(rut[5])*3)+(int(rut[6])*2))
    b=a%11
    c=11-b
    if c==10:
        print("dv=k")
    elif c==11:
        print("dv=0")
    else:
        print("dv="+str(c))

