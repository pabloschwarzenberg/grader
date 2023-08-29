#Sistema de Ecuaciones
c1=float(input())
c2=float(input())
c3=float(input())
c4=float(input())
c5=float(input())
c6=float(input())



if c1-c4==0:
    SolucionY=(c3-c6)/(c2-c5)
    print("y=",SolucionY)
else:
    if c2-c5==0:
        SolucionX=(c3-c6)/(c1-c4)
        print("x=",SolucionX)
    else:
        SX=(c6*c2-c5*c3)/(c2*c4-c5*c1)
        SY=(c6*c1-c4*c3)/(c5*c1-c2*c4)
        print("x=",SX)
        print("y=",SY)
