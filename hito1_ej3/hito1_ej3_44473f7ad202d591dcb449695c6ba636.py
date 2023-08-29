#Aprobación de créditos
ingreso = eval(input("Ingresa tus Ingresos en pesos chilenos:\n"))
añona = eval(input("Ingresa tu año de nacimiento:\n"))
nhijos = eval(input("Ingresa el número de hijos:\n"))
pert = eval(input("Ingresa tus años de pertenencia al banco:\n"))
ec = str(input("Ingresa tu estado civil\n soltero o casado:\n"))
vive = str(input("Ingresa si vives en campo o ciudad\n U:Ciudad | R:Campo\n"))
if (pert > 10) and (nhijos >= 2):
    print("APROBADO")
elif (ec == "casado") and (nhijos > 3) and añona == range(1966,1976):
    print("APROBADO")
elif (ingreso > 2500000) and (ec == "soltero") and (vive == "U"):
    print("APROBADO")
elif (ingreso > 3500000) and (pert > 5):
    print("APROBADO")
elif (vive == "R") and (ec == "casado") and (nhijos < 2):
    print("APROBADO")
else:
    print("NO APROBADO")