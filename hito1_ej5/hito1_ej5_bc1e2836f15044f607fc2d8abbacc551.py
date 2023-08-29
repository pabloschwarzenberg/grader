#Cálculo del dígito verificador de un rut
rut=str(input("Rut:"))
n=int(rut[len(rut)-1])
if len(rut)==8:
    n_1=int(rut[len(rut)-2])
    n_2=int(rut[len(rut)-3])
    n_3=int(rut[len(rut)-4])
    n_4=int(rut[len(rut)-5])
    n_5=int(rut[len(rut)-6])
    n_6=int(rut[len(rut)-7])
    n_7=int(rut[len(rut)-8])
    suma=n*2+n_1*3+n_2*4+n_3*5+n_4*6+n_5*7+n_6*2+n_7*3
    dv=11-(suma%11)
    if dv==11:
        print("dv=0")
    else:
        if dv==10:
            print("dv=k")
        else:
            print("dv=",dv)
else:
    n_1=int(rut[len(rut)-2])
    n_2=int(rut[len(rut)-3])
    n_3=int(rut[len(rut)-4])
    n_4=int(rut[len(rut)-5])
    n_5=int(rut[len(rut)-6])
    n_6=int(rut[len(rut)-7])
    suma=n*2+n_1*3+n_2*4+n_3*5+n_4*6+n_5*7+n_6*2
    dv=11-(suma%11)
    if dv==11:
        print("dv=0")
    else:
        if dv==10:
            print("dv=k")
        else:
            print("dv=",dv)