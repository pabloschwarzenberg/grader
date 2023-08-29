ing= int(input("dame tu ingreso(en pesos)"))
ano = int(input("año de nacimiento?"))
hijos= int(input("numero de hijos"))
pert = int(input("años de pertenencia en el banco"))
esta = input("estado civil")
vivi =input("campo o ciudad?")


aprob="no"


if pert > 10:
    aprob="si"

if esta == "C" and hijos>3 and 45<ano<55:
    aprob="si"

if ing > 3500000 and pert>5:
    aprob="si"

if vivi == "R" and esta == "C" and hijos<2:
    aprob="si"


if aprob=="si":
    print("APROBADO")

else:
    print("RECHAZADO")    
