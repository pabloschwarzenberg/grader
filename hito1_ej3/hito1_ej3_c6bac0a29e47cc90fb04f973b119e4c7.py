#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso:"))
año_nacimiento = int(input("Ingrese su año de nacimiento:"))
num_hijos = int(input("Ingrese cuantos hijos tiene usted:"))
años_pert_banco = int(input("Ingrese su antiguedad en el banco:"))
estado_civil = input("Indique su Estado Civil / Soltero o Casado:")
residencia = input("¿En que lugar vive?:")

año_actual=2020
edad = año_actual-año_nacimiento
if (años_pert_banco>10 and num_hijos>=2) or(estado_civil=="C" and num_hijos>3 and (edad>45 or edad<55)) or \
    (ingreso>2500000 and estado_civil=="S" and residencia=="U") or \
    (ingreso>3500000 and años_pert_banco>5) or \
    (residencia=="R" and estado_civil=="C" and num_hijos<2):

    print("APROBADO")     