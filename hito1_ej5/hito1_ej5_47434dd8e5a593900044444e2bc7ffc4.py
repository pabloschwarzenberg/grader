rut=str(input("Ingresa los digitos de tu rut: "))
if len(rut)==7:
    s=int(rut[0])*2+int(rut[1])*7+int(rut[2])*6+int(rut[3])*5+int(rut[4])*4+int(rut[5])*3+int(rut[6])*2
    pe=s//11
    r=s-(11*pe)
    final=11-r
    if final==11:
        print("dv=0")
    if final==10:
        print("dv=K")
    else:
        print("dv="+str(final))
if len(rut)==8:
    s=int(rut[0])*3+int(rut[1])*2+int(rut[2])*7+int(rut[3])*6+int(rut[4])*5+int(rut[5])*4+int(rut[6])*3+int(rut[7])*2
    pe=s//11
    r=s-(11*pe)
    final=11-r
    if final==11:
        print("dv=0")
    if final==10:
        print("dv=K")
    else:
        print("dv=",str(final))   
        