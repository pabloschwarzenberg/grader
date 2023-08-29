rut=str(input("RUT :"))

if len(rut)==8:
    rut1=int(rut[-1])*2
    rut2=int(rut[-2])*3
    rut3=int(rut[-3])*4
    rut4=int(rut[-4])*5
    rut5=int(rut[-5])*6
    rut6=int(rut[-6])*7
    rut7=int(rut[-7])*2
    rut8=int(rut[-8])*3

    suma_rut=rut1+rut2+rut3+rut4+rut5+rut6+rut7+rut8
    div_rut=round((suma_rut//11),0)
    rut_new=11-(suma_rut-(11*div_rut))
    rut_new_new=0
    if rut_new==11:
        rut_new_new=0
    if rut_new==10:
        rut_new_new="K"
    if rut_new>=1 and rut_new<=9:
        rut_new_new=rut_new

    print("dv="+str(rut_new_new))

if len(rut)==7:
    rut1=int(rut[-1])*2
    rut2=int(rut[-2])*3
    rut3=int(rut[-3])*4
    rut4=int(rut[-4])*5
    rut5=int(rut[-5])*6
    rut6=int(rut[-6])*7
    rut7=int(rut[-7])*2

    suma_rut=rut1+rut2+rut3+rut4+rut5+rut6+rut7
    div_rut=round((suma_rut//11),0)
    rut_new=11-(suma_rut-(11*div_rut))
    rut_new_new=0
    if rut_new==11:
        rut_new_new=0
    if rut_new==10:
        rut_new_new="K"
    if rut_new>=1 and rut_new<=9:
        rut_new_new=rut_new

    print("dv="+str(rut_new_new))