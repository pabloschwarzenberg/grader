#Aprobación de créditos
Ing = float(input("Ingrese sus ingresos en pesos: "))
Nacim = float(input("Ingrese su año de nacimiento: "))
Hijos = float(input("Ingrese el número de hijos que tiene: "))
anospert = float(input("Ingrese los años de pertenencia al banco: "))
EstCivil = str(input("Indique su estado civil, (S) soltero y (C) casado: "))
CampoOciudad = str(input("Indique si vive en campo o ciudad (U) urbano y (R) rural: "))
edad = 2021-Nacim
if (anospert>10) and (Hijos>2):
    print ("APROBADO")
elif EstCivil=="C" or "c" and (Hijos>3) and (45>=edad<=55):
    print("APROBADO")
elif (Ing>2500000) and (EstCivil== "S" or "s") and (CampoOciudad=="U" or "u"):
    print("APROBADO")
elif (Ing>3500000) and anospert>5:
    print("APROBADO")
elif CampoOciudad=="R" or "r" and EstCivil=="C" or "c" and Hijos<2:
    print("APROBADO")
else:
    print("RECHAZADO")