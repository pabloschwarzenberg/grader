#Cálculo del dígito verificador de un rut
rut= input("Ingrese su rut: ")
rut_lista = []

for i in rut:
    rut_lista.append(int(i))
if len(rut_lista) == 8:    
    f = (rut_lista[7])*2 + (rut_lista[6])*3 + (rut_lista[5])*4 + (rut_lista[4])*5 + (rut_lista[3])*6 + (rut_lista[2])*7 + (rut_lista[1])*2 + (rut_lista[0])*3
    ff = 11 - (f-(11*(f//11)))
    if ff == 11:
        print("dv=0")
    elif ff == 10:
        print("dv=k")
    else:
        print("dv=",ff)
elif len(rut_lista)== 7:
    f = (rut_lista[6])*2 + (rut_lista[5])*3 + (rut_lista[4])*4 + (rut_lista[3])*5 + (rut_lista[2])*6 + (rut_lista[1])*7 + (rut_lista[0])*2
    ff = 11 - (f-(11*(f//11)))
    if ff == 11:
        print("dv=0")
    elif ff == 10:
        print("dv=k")
    else:
        print("dv=",ff)