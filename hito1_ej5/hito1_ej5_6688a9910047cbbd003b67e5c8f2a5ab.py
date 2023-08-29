rut=str(input("Ingrese su numero de rut: "))
if len(rut)==8:
    a=int(rut[0])
    b=int(rut[1])
    c=int(rut[2])
    d=int(rut[3])
    e=int(rut[4])
    f=int(rut[5])
    g=int(rut[6])
    h=int(rut[7])
    S=int(h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3)
    R=int(S%11)
    dv=int(11-R)
    if (dv==10):
        print("dv=k")
    elif (dv==11):
        print("dv=11")
    else:
        print("dv=",dv)
if len(rut)==7:
    a=int(rut[0])
    b=int(rut[1])
    c=int(rut[2])
    d=int(rut[3])
    e=int(rut[4])
    f=int(rut[5])
    g=int(rut[6])
    S=int(g*2+f*3+e*4+d*5+c*6+b*7+a*2)
    R=int(S%11)
    dv=int(11-R)
    if (dv==10):
        print("dv=k")
    elif (dv==11):
         print("dv=0")
    else:
         print("dv=",dv)

