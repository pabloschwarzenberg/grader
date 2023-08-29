#Cálculo del dígito verificador de un rut
rut=int(input("Ingrese el RUT sin dígito verificador: "))

aux1=rut%10
dg1=aux1*2
aux2=(rut%100)-aux1
dg2=(aux2//10)*3
aux3=(rut%1000)-aux2
dg3=(aux3//100)*4
aux4=(rut%10000)-aux3
dg4=(aux4//1000)*5
aux5=(rut%100000)-aux4
dg5=(aux5//10000)*6
aux6=(rut%1000000)-aux5
dg6=(aux6//100000)*7
aux7=(rut%10000000)-aux6
dg7=(aux7//1000000)*2
aux8=(rut%100000000)-aux7
dg8=(aux8//10000000)*3

suma=(dg1+dg2+dg3+dg4+dg5+dg6+dg7+dg8)%11
dv=11-suma

if dv>9:
    if dv==11:
        print("dv=0")
    elif dv==10:
        print("dv=K")
else:
    print("dv=",dv)
