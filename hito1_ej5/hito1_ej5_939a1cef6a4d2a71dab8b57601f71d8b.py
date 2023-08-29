#Cálculo del dígito verificador de un rut
rut=input()
largo=len(rut)
if largo==8:
    a=int(rut[0])
    b=int(rut[1])
    c=int(rut[2])
    d=int(rut[3])
    e=int(rut[4])
    f=int(rut[5])
    g=int(rut[6])
    h=int(rut[7])
    verificador=h*2+g*3+f*4+e*5+d*6+c*7+b*2+a*3
    modulo11=verificador%11
    final=int(11-modulo11)
    if final==11:
        print(0)
    else:
        if final==10:
            print("dv=K")
        else:
            print(final)
else:
    a=int(rut[0])
    b=int(rut[1])
    c=int(rut[2])
    d=int(rut[3])
    e=int(rut[4])
    f=int(rut[5])
    g=int(rut[6]) 
verificador=g*2+f*3+e*4+d*5+c*6+b*7+a*2
modulo11=verificador%11
final=int(11-modulo11)
if final==11:
    print("dv=0")
else:
    if final==10:
        print("dv=K")
    else:
        print("dv={0}".format(final)) 