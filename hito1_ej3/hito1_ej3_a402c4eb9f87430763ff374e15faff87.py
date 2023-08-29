#Aprobación de créditos
print("Con el fin de aprobar su crédito ingrese la siguiente información")
ingreso = int(input("Ingrese su ingreso $ "))
ano_nacimiento = int(input("Año de nacimiento "))
numero_hijos = int(input("Número de hijos "))
ano_pertenencia = int(input("Año de pertenencia al banco "))
estado_civil = str(input("Ingrese 'S': soltero, 'C', casado "))
vive = str(input("Ingrese 'U': urbano, 'R': rural "))
edad = 2021 - ano_nacimiento

if ano_pertenencia > 10 and numero_hijos >= 2:
    print("APROBADO")
if estado_civil == "C" and numero_hijos > 3 and 45 > edad < 55:
    print("APROBADO")
if ingreso > 2500000 and estado_civil == "S" and vive == "U":
    print("APROBADO")
if ingreso > 3500000 and ano_pertenencia > 5:
    print ("APROBADO")
if vive == "R" and estado_civil == "C" and numero_hijos <2:
    print("APROBADO")
else:
        print("RECHZADO")
