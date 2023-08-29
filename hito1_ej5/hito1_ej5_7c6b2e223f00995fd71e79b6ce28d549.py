#Cálculo del dígito verificador de un rut
N=int(input("Ingrese RUT sin dígito verificador:"))
if N/10000000>=1:
    N=str(N)
    d8=int(N[-1])
    d7=int(N[-2])
    d6=int(N[-3])
    d5=int(N[-4])
    d4=int(N[-5])
    d3=int(N[-6])
    d2=int(N[-7])
    d1=int(N[-8])

    d8=d8*2
    d7=d7*3
    d6=d6*4
    d5=d5*5
    d4=d4*6
    d3=d3*7
    d2=d2*2
    d1=d1*3

    s=d8+d7+d6+d5+d4+d3+d2+d1

    r=s%11

    dv=11-r
    if dv!=10 and dv!=11:
        print("dv=",dv)
    elif dv==11:
        print("dv=","0")
    elif dv==10:
        print("dv=","k")

elif N/10000000<1:
    N=str(N)

    d8=int(N[-1])
    d7=int(N[-2])
    d6=int(N[-3])
    d5=int(N[-4])
    d4=int(N[-5])
    d3=int(N[-6])
    d2=int(N[-7])

    d8=d8*2
    d7=d7*3
    d6=d6*4
    d5=d5*5
    d4=d4*6
    d3=d3*7
    d2=d2*2

    s=d8+d7+d6+d5+d4+d3+d2

    r=s%11

    dv=11-r

    if dv!=10 and dv!=11:
        print("dv=",dv)
    elif dv==11:
        print("dv=","0")
    elif dv==10:
        print("dv=","k")   