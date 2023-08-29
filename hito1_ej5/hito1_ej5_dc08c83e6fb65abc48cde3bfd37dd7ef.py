#Cálculo del dígito verificador de un rut
rut=input()
digito=len(rut)
if digito==8:
    n1=rut[0]
    n2=rut[1]
    n3=rut[2]
    n4=rut[3]
    n5=rut[4]
    n6=rut[5]
    n7=rut[6]
    n8=rut[7]
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    n4=int(n4)
    n5=int(n5)
    n6=int(n6)
    n7=int(n7)
    n8=int(n8)
    n1=n1*3
    n2=n2*2
    n3=n3*7
    n4=n4*6
    n5=n5*5
    n6=n6*4
    n7=n7*3
    n8=n8*2
    nsuma=(n1+n2+n3+n4+n5+n6+n7+n8)
    nresto=nsuma%11
    nfinal=11-nresto
    if nfinal==11:
        print("dv=0")
    if nfinal==10:
        print("dv=k")
    else:
        print("dv=",nfinal)
if digito==7:
    n1=rut[0]
    n2=rut[1]
    n3=rut[2]
    n4=rut[3]
    n5=rut[4]
    n6=rut[5]
    n7=rut[6]
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    n4=int(n4)
    n5=int(n5)
    n6=int(n6)
    n7=int(n7)
    n1=n1*2
    n2=n2*7
    n3=n3*6
    n4=n4*5
    n5=n5*4
    n6=n6*3
    n7=n7*2
    nsuma=(n1+n2+n3+n4+n5+n6+n7)
    nresto=nsuma%11
    nfinal=11-nresto
    if nfinal==11:
        print("dv=0")
    elif nfinal==10:
        print("dv=k")
    else:
        print("dv=",nfinal)      