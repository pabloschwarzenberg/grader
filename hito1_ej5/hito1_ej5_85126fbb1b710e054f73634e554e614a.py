rut=input("ingrese su rut: ")
if len(rut)==8:
    a=int(rut[7])*2
    b=int(rut[6])*3
    c=int(rut[5])*4
    d=int(rut[4])*5
    e=int(rut[3])*6
    f=int(rut[2])*7
    g=int(rut[1])*2
    h=int(rut[0])*3
    i=a+b+c+d+e+f+g+h
    j=i%11
    k=11-j
    print("dv=",k)
    if k==10:
        print("dv=","k")
elif len(rut)==7:
    a=int(rut[6])*2
    b=int(rut[5])*3
    c=int(rut[4])*4
    d=int(rut[3])*5
    e=int(rut[2])*6
    f=int(rut[1])*7
    g=int(rut[0])*2
    i=a+b+c+d+e+f+g
    j=i%11
    k=11-j
    if k==11:
        print("dv=",0)
    if k==10:
        print("dv=","k")
    if k!=11:
        print("dv=",k)

