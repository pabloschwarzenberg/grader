ingreso = float(input("Digite su ingreso:"))
nacimiento = int(input("Ingrese su año de nacimiento:"))
nhijos = int(input("Ingrese el numero de hijos que tiene:"))
anos = int(input("Ingrese los años de pertenencia al banco: "))
estadocivil = input("Ingrese su estado civil,digite S si es solero o C si es casado: ")
vive = input("Ingrese si vive en campo o ciudad, U urbano o R rural: ")
edad = 2020 - nacimiento
if (anos>10) and (nhijos >=2):
    print("APROBADO")
elif (estadocivil == "C") and (nhijos > 3 ) and (edad >=45 and edad <=55):
    print("APROBADO")
elif (ingreso > 2500000) and (estadocivil == "S") and (vive == "U"):
    print("APROBADO")
elif (ingreso > 3500000) and (anos >5):
    print("APROBADO")
elif (vive == "R") and (estadocivil == "C") and (nhijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")