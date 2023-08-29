#Cálculo del dígito verificador de un rut
rut= str(input())
q=0
w=0
e=0
r=0
t=0
y=0
u=0
i=0
sumando = 0
resto = 0
if len(rut) == 7:
    q=int(rut[6])*2
    w=int(rut[5])*3
    e=int(rut[4])*4
    r=int(rut[3])*5
    t=int(rut[2])*6
    y=int(rut[1])*7
    u=int(rut[0])*2
    sumando = q+w+e+r+t+y+u
    resto = sumando % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=k")
    else:
        print("dv=",dv)
elif len(rut) == 8:
    q=int(rut[7])*2
    w=int(rut[6])*3
    e=int(rut[5])*4
    r=int(rut[4])*5
    t=int(rut[3])*6
    y=int(rut[2])*7
    u=int(rut[1])*2
    i=int(rut[0])*3
    sumando = q+w+e+r+t+y+u+i
    resto = sumando % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=k")
    else:
        print("dv:",dv)
elif len(rut) == 9:
    q=int(rut[8])*2
    w=int(rut[7])*3
    e=int(rut[6])*4
    r=int(rut[5])*5
    t=int(rut[4])*6
    y=int(rut[3])*7
    u=int(rut[2])*2
    i=int(rut[1])*3
    o=int(rut[0])*4
    sumando = q+w+e+r+t+y+u+i+o
    resto = sumando % 11
    dv = 11 - resto
    if dv == 11:
        print("dv=0")
    elif dv == 10:
        print("dv=k")
    else:
        print("dv=",dv)
else:
    print("rut no valido")
