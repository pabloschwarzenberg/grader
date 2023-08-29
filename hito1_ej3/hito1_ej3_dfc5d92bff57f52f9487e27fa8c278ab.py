#Aprobación de créditos

ingr = eval(input("Ingrese su Ingreso monetario mensual : $"))
ano_nac = eval(input("Ingrese su año de nacimiento: "))
cant_hijos = eval(input("Ingrese la cantidad de hijos que tenga: "))
anos_pert = eval(input("Ingrese los años de pertenencia al banco que tenga: "))
est_civil = (input("Ingrese su estado civil (S: soltero) (C: casado): "))
camp_ciud = input("Ingrese si vive en campo o cuidad (U: urbano) (R: rural): ")

est_civil = "S" or "C"
camp_ciud = "U" or "R"
edad = (2020 - ano_nac)

if (anos_pert > 10 and cant_hijos >= 2):
    print("APROBADO")
elif (est_civil == "C" and cant_hijos > 3 and (45 < edad < 55)):
    print("APROBADO")
elif(ingr > 2500000 and est_civil == "S" and camp_ciud == "U"):
    print("APORBADO")
elif(ingr > 3500000 and anos_pert > 5):
    print("APROBADO")
elif(camp_ciud == "R" and est_civil == "C" and cant_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")
