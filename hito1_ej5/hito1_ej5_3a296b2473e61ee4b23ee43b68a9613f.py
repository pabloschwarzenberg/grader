rut = str(input("Ingrse su rut sin digito verificador, ni puntos:"))
if len(rut)==8:
    rinv = rut[::-1]
    n1=int(rinv[0])*2
    n2=int(rinv[1])*3
    n3=int(rinv[2])*4
    n4=int(rinv[3])*5
    n5=int(rinv[4])*6
    n6=int(rinv[5])*7
    n7=int(rinv[6])*2
    n8=int(rinv[7])*3
    
    sumatoria = n1+n2+n3+n4+n5+n6+n7+n8
    sobra = sumatoria%11
    divisor = 11-sobra

    if divisor==10:
        print("dv= K")
    elif divisor==11:
        print("dv= 0")
    else:
        print("dv=",divisor)

elif len(rut)==7:
    rinv = rut[::-1]
    n1=int(rinv[0])*2
    n2=int(rinv[1])*3
    n3=int(rinv[2])*4
    n4=int(rinv[3])*5
    n5=int(rinv[4])*6
    n6=int(rinv[5])*7
    n7=int(rinv[6])*2

    sumatoria = n1+n2+n3+n4+n5+n6+n7
    sobra = sumatoria%11
    divisor = 11-sobra

    if divisor==10:
        print("dv=K")
    elif divisor==11:
        print("dv=0")
    else:
        print("dv=",divisor)
