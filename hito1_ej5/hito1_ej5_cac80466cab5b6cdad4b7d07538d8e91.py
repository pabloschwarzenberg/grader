rut=input("Ingrese su rut: ")
srut = str(rut)
l = len(srut)
if(l == 8):
    d7 = int((rut[7]))*2
    d6 = int((rut[6]))*3
    d5 = int((rut[5]))*4
    d4 = int((rut[4]))*5
    d3 = int((rut[3]))*6
    d2 = int((rut[2]))*7
    d1 = int((rut[1]))*2
    d0 = int((rut[0]))*3
    suma=d7+d6+d5+d4+d3+d2+d1+d0
    ent=suma//11
    res=suma-(11*ent)
    dv=11-res
    if dv==11:
        dv=0
    if dv==10:
        dv="K"
    print("dv=",dv)
if (l == 7):
    d6 = int((rut[6]))*2
    d5 = int((rut[5]))*3
    d4 = int((rut[4]))*4
    d3 = int((rut[3]))*5
    d2 = int((rut[2]))*6
    d1 = int((rut[1]))*7
    d0 = int((rut[0]))*2
    suma=d6+d5+d4+d3+d2+d1+d0
    ent=suma//11
    res=suma-(11*ent)
    dv=11-res
    if dv==11:
        dv=0
    if dv==10:
        dv="k"
    print("dv=",dv)