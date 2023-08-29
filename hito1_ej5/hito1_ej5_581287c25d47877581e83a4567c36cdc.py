rut=str(input("6016740"))
digitos=len(str(rut))
if digitos==8:
    n1=rut[0:1]
    n2=rut[1:2]
    n3=rut[2:3]
    n4=rut[3:4]
    n5=rut[4:5]
    n6=rut[5:6]
    n7=rut[6:7]
    n8=rut[7:8]
    m1=2*int(n8)
    m2=3*int(n7)
    m3=4*int(n6)
    m4=5*int(n5)
    m5=6*int(n4)
    m6=7*int(n3)
    m7=2*int(n2)
    m8=3*int(n1)
elif digitos==7:
    n1=rut[0:1]
    n2=rut[1:2]
    n3=rut[2:3]
    n4=rut[3:4]
    n5=rut[4:5]
    n6=rut[5:6]
    n7=rut[6:7]
    m1=2*int(n7)
    m2=3*int(n6)
    m3=4*int(n5)
    m4=5*int(n4)
    m5=6*int(n3)
    m6=7*int(n2)
    m7=2*int(n1)
    m8=3*0

suma=m1+m2+m3+m4+m5+m6+m7+m8
ent=suma/11
ent=int(ent)
div=suma-(11*ent)
dv=11-div
if dv==11:
    print("dv=0")
else:
    if dv==10:
        print("dv=k")
    else:
        print("dv=",dv,sep="")
