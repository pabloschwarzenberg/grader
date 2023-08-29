#Aprobación de créditos
ingreso = float(input("Ingreso: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Números de hijos: "))
pertenencia = int(input("Años de pertenencia al banco: "))
estadocivil = input("Estado civil ('S': Soltero, 'C': Casado): ")
vive = input("Vive en campo o ciudad ('U': Urbano, 'R': Rural): ")
edad = 2022 - nacimiento

if pertenencia > 10 and hijos >= 2:
 print("APROBADO")
elif (estadocivil == "C" or estadocivil == "c") and (edad >= 45 and edad <= 55) and (hijos > 3):
 print("APROBADO")
elif (ingreso > 2500000) and (estadocivil == "S" or estadocivil == "s") and (vive == "U" or vive == "u"):
 print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
 print("APROBADO")
elif vive == "R" and (estadocivil == "C" or estadocivil == "c") and hijos < 2:
 print("APROBADO")
else:
 print("RECHAZADO")