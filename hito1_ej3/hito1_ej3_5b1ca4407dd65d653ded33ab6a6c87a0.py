#Aprobación de créditos
ingreso=int(input("Ingrese su ingreso:"))
año_nacimiento=int(input("Ingrese su año de nacimiento:"))
num_hijos=int(input("Ingrese la cantidad de hijos:"))
años_pert_banco=int(input("Ingrese los años de pertenencia al banco:"))
estado_civil=input("¿Cuál es su estado civil? S/C:")
residencia=input("¿En qué zona vive? U/R:")


año_actual=2020
edad=año_actual-año_nacimiento
if (años_pert_banco>10 and num_hijos>=2) or(estado_civil=="C" and num_hijos>3 and (edad>45 or edad<55)) or \
   (ingreso>2500000 and estado_civil=="S" and residencia=="U") or \
   (ingreso>3500000 and años_pert_banco>5) or \
   (residencia=="R" and estado_civil=="C" and num_hijos<2):

    print("APROBADO")

else:
    print("RECHAZADO") 