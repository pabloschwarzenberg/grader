#Cálculo del dígito verificador de un rut
RUT=(input("Ingrese su RUT: "))
largo=len(RUT)
print(largo)
if largo==8:
    v=RUT[0]
    V=int(v)*3
    v1=RUT[1]
    V1=int(v1)*2
    v2=RUT[2]
    V2=int(v2)*7
    v3=RUT[3]
    V3=int(v3)*6
    v4=RUT[4]
    V4=int(v4)*5
    v5=RUT[5]
    V5=int(v5)*4
    v6=RUT[6]
    V6=int(v6)*3
    v7=RUT[7]
    V7=int(v7)*2
    DV=(V+V1+V2+V3+V4+V5+V6+V7)
    R=(DV/11)   
    r=DV%11
    R2=DV-(11*r)
    dv=11-r
    if dv==11:
        print("dv=0")
    elif dv==10:
        print("dv=K")
    else:
        print("dv=",dv)
else:
    largo==7
    v=RUT[0]
    V=int(v)*2
    v1=RUT[1]
    V1=int(v1)*7
    v2=RUT[2]
    V2=int(v2)*6
    v3=RUT[3]
    V3=int(v3)*5
    v4=RUT[4]
    V4=int(v4)*4
    v5=RUT[5]
    V5=int(v5)*3
    v6=RUT[6]
    V6=int(v6)*2
    DV=(V+V1+V2+V3+V4+V5+V6)
    R=(DV/11)   
    r=DV%11
    R2=DV-(11*r)
    dv=11-r
    if dv==11:
        print("dv=0")
    elif dv==10:
        print("dv=K")
    else:
        print("dv=",dv)
