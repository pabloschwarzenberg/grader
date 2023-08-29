#Cálculo del dígito verificador de un rut
rut = input("Ingrese su rut")
if len(rut)== 8:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])
    n7 = int(rut[6])
    n8 = int(rut[7])

    calculo1= n8*2 + n7*3 + n6*4 + n5*5 + n4*6 + n3*7 + n2*2 + n1*3


    calculo2= calculo1%11

    dv= 11-calculo2

    if dv == 11 or dv == 10:
        if dv == 10:
         dv = "k"
         print("dv="+str(dv))
        if dv == 11:
         cv = 0
         print("dv="+str(dv))

    else:
        print("dv="+str(dv))
         

else:
    n1 = int(rut[0])
    n2 = int(rut[1])
    n3 = int(rut[2])
    n4 = int(rut[3])
    n5 = int(rut[4])
    n6 = int(rut[5])
    n7 = int(rut[6])

    calculo1= n7*2 + n6*3 + n5*4 + n4*5 + n3*6 + n2*7 + n1*2
    calculo2= calculo1%11

    dv= 11-calculo2

    if dv == 11 or dv == 10:
        if dv == 10:
         dv = "k"
         print("dv="+str(dv))
        if dv == 11:
         dv = 0
         print("dv="+str(dv))
   
    else:
        print("dv="+str(dv))
