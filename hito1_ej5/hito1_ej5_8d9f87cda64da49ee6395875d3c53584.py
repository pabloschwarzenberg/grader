#Cálculo del dígito verificador de un rut
rut = str(input("Ingrese RUT sin dígito verificador y sin puntos:"))
a = rut[0:8]
b = rut[0:7]
if len(rut)==8:
    s1 = int(a[7])*2
    s2 = int(a[6])*3
    s3 = int(a[5])*4
    s4 = int(a[4])*5
    s5 = int(a[3])*6
    s6 = int(a[2])*7
    s7 = int(a[1])*2
    s8 = int(a[0])*3
    suma1 = s1+s2+s3+s4+s5+s6+s7+s8
    resto1 = suma1%11
    resta1 = (11-resto1)
    if (resta1==10):
        print("dv=K")
        if (resta1==11):
            print("dv=0")
    else:
        print("dv=",resta1)
else:
    if len(rut)==7:
        s9 = int(b[6])*2
        s10 = int(b[5])*3
        s11 = int(b[4])*4
        s12 = int(b[3])*5
        s13 = int(b[2])*6
        s14 = int(b[1])*7
        s15 = int(b[0])*2
        suma2 = s9+s10+s11+s12+s13+s14+s15
        resto2 = suma2%11
        resta2 = (11-resto2)
        if (resta2==11):
            print("dv=0")
            if (resta2==10):
                print("dv=K")
        else:
            print("dv=", resta2)