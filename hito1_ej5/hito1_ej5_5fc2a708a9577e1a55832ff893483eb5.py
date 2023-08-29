rut=input("Ingrese rut: ")
if len(rut)==8:
    d1=int(rut[-1])
    d2=int(rut[-2])
    d3=int(rut[-3])
    d4=int(rut[-4])
    d5=int(rut[-5])
    d6=int(rut[-6])
    d7=int(rut[-7])
    d8=int(rut[-8])

    S=(d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2 + d8*3)
    R=str(11-S%11)
    if R=="11":
        print("dv="+"0")
    if R!=str(10):
        print("dv="+R)
    else:
        print("dv="+"k")
if len(rut)==7:
    d1=int(rut[-1])
    d2=int(rut[-2])
    d3=int(rut[-3])
    d4=int(rut[-4])
    d5=int(rut[-5])
    d6=int(rut[-6])
    d7=int(rut[-7])
    S=(d1*2 + d2*3 + d3*4 + d4*5 + d5*6 + d6*7 + d7*2)
    R=str(11-S%11)
    if R=="11":
        print("dv="+"0")
    elif R!=str(10):
        print("dv="+R)
    else:
        print("dv="+"k")