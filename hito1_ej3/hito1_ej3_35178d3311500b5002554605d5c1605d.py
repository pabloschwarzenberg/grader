#Aprobación de créditos
#Entradas 
#Aprobación de créditos
#Entradas 
ingreso = int(input("Ingrese su ingreso: "))
año = int(input("Ingrese su año de nacimiento: "))
num_hijos = int(input("Ingrese su numero de hijos: "))
años_banco = int(input("Ingrese su numero de años de pertenencia al banco: "))
edo_civil = input("Ingrese su estado civil (S/C)")
casa = input("Indique si vive en un lugar urbano o rural(U/R)")
edad = 2020-año

if años_banco >= 10 and num_hijos >= 2:
    print("APROBADO")
elif edo_civil == "C" and num_hijos > 3 and (edad>=45 and edad<=55):
    print("APROBADO")
elif ingreso> 2500000 and edo_civil == "S" and casa == "U":
    print ("APROBADO")
elif ingreso> 2500000 and años_banco >= 5:
    print("APROBADO")
elif casa == "R" and edo_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print ("RECHAZADO")
