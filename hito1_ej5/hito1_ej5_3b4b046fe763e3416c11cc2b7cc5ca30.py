#Cálculo del dígito verificador de un rut
rut=str(input())
if len(rut)==8:
    d1=int(rut[0])
    d2=int(rut[1])
    d3=int(rut[2])
    d4=int(rut[3])
    d5=int(rut[4])
    d6=int(rut[5])
    d7=int(rut[6])
    d8=int(rut[7])
    d8=d8*2
    d7=d7*3
    d6=d6*4
    d5=d5*5
    d4=d4*6
    d3=d3*7
    d2=d2*2
    d1=d1*3
    s=d1+d2+d3+d4+d5+d6+d7+d8
    s=11-s%11
    if s==11:
        dv=0
        print("dv=",dv)
    if s==10:
        dv='K'
        print("dv=",dv)
    else:
        print("dv=",s)
if len(rut)==7:
    d1=int(rut[0])
    d2=int(rut[1])
    d3=int(rut[2])
    d4=int(rut[3])
    d5=int(rut[4])
    d6=int(rut[5])
    d7=int(rut[6])
    d7=d7*2
    d6=d6*3
    d5=d5*4
    d4=d4*5
    d3=d3*6
    d2=d2*7
    d1=d1*2
    s=d1+d2+d3+d4+d5+d6+d7
    s=11-s%11
    if s==11:
        dv=0
        print("dv=",dv)
    if s==10:
        dv='K'
        print("dv=",dv)
    else:
        print("dv=",s)