rut=input("ingrese rut:")
if len(rut)==8:
    a=int(rut[7])*2
    b=int(rut[6])*3
    c=int(rut[5])*4
    d=int(rut[4])*5
    e=int(rut[3])*6
    f=int(rut[2])*7
    g=int(rut[1])*2
    h=int(rut[0])*3
    suma=a+b+c+d+e+f+g+h
    dv=(11)-(suma-(11*(int(suma/11))))
    
    
    if dv==11:
        print("dv=0")
    elif dv==10:
        print("dv=k")
    elif dv!=11 and dv!=10:
        print("dv={0}".format(dv))
elif len(rut)==7:
    a=int(rut[6])*2
    b=int(rut[5])*3
    c=int(rut[4])*4
    d=int(rut[3])*5
    e=int(rut[2])*6
    f=int(rut[1])*7
    g=int(rut[0])*2
    suma=a+b+c+d+e+f+g
    dv=(11)-(suma-(11*(int(suma/11))))
   
    
    
    if dv==11:
        print("dv=0")
    elif dv==10:
        print("dv=k")
    elif dv!=11 and dv!=10:
        print("dv={0}".format(dv))
else :
    print("ingrese un rut valido")
