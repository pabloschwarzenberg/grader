rut=(input("Ingresa el rut sin numero verificador: "))
if len(rut)==8:
    suma=int(rut[7])*2+int(rut[6])*3+int(rut[5])*4+int(rut[4])*5+int(rut[3])*6+int(rut[2])*7+int(rut[1])*2+int(rut[0])*3
    partentera=(suma//11)
    resto=(suma-(11*partentera))
    x=(11-resto)
    if x==11:
        print("dv=","0")
    elif x==10:
        print("dv=","k")
    else:
        print("dv=",int(x))
if len(rut)==7:
    suma=int(rut[6])*2+int(rut[5])*3+int(rut[4])*4+int(rut[3])*5+int(rut[2])*6+int(rut[1])*7+int(rut[0])*2
    partentera=(suma//11)
    resto=(suma-(11*partentera))
    x=(11-resto)
    if x==11:
        print("dv=","0")
    elif x==10:
        print("dv=","k")
    else:
        print("dv=",int(x))
    
      