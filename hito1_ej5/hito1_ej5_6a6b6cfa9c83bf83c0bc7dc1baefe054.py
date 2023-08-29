        #Cálculo del dígito verificador de un rut
R=str(input("Escriba su RUN sin digito verificador"))
N=len(R)
if N==8:
    x8=int(R[7])
    x7=int(R[6])
    x6=int(R[5])
    x5=int(R[4])
    x4=int(R[3])
    x3=int(R[2])
    x2=int(R[1])
    x1=int(R[0])
    serie=float((x1*3)+(x2*2)+(x3*7)+(x4*6)+(x5*5)+(x6*4)+(x7*3)+(x8*2))
    d=int(11-(serie%11))
    if d==11:
            print("dv=0")
    elif d==10:
            print("dv=k")
    else:
            print("dv=",d)
elif N==7:
    R="0"+R
    x8=int(R[7])
    x7=int(R[6])
    x6=int(R[5])
    x5=int(R[4])
    x4=int(R[3])
    x3=int(R[2])
    x2=int(R[1])
    x1=int(R[0])
    serie=float((x1*3)+(x2*2)+(x3*7)+(x4*6)+(x5*5)+(x6*4)+(x7*3)+(x8*2))
    d=int(11-(serie%11))
    if d==11:
            print("dv=0")
    elif d==10:
            print("dv=k")
    else:
            print("dv=",d)
else:
    print("Escriba un rut valido!")