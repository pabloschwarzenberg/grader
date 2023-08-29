#Cálculo del dígito verificador de un rut
#definir para rut de 7 digitos.
a=input("ingrese RUT: ")
if int(a)>9999999:
    a0=int(a[0])
    a1=int(a[1])
    a2=int(a[2])
    a3=int(a[3])
    a4=int(a[4])
    a5=int(a[5])
    a6=int(a[6])
    a7=int(a[7])

    v1=(a0*8)+(a1*9)+(a2*4)+(a3*5)+(a4*6)+(a5*7)+(a6*8)+(a7*9)
    v2=v1%11
    if v2!=10:
        print("dv=", v2)
    else:
        print("dv=k")
else:
    a0=int(a[0])
    a1=int(a[1])
    a2=int(a[2])
    a3=int(a[3])
    a4=int(a[4])
    a5=int(a[5])
    a6=int(a[6])

    v1=(a0*9)+(a1*4)+(a2*5)+(a3*6)+(a4*7)+(a5*8)+(a6*9)
    v2=v1%11
    if v2!=10:
        print("dv=", v2)
    else:
        print("dv=k")