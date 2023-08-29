#Aprobación de créditos


ing = int(input("Número de ingresos: "))
print("")
nac = int(input("Año de nacimiento:  "))
print("")
hijos = int(input("Número de hijos: "))
print("")
años = int(input("Años de pertenencia al banco: "))
print("")
print("S = soltero \n C = Casado")
print("")
civil = input("Estado Civil: ")
print("")
print("U = Urbano \n R = Rural")
print("")
sector = input("Sector de vivienda: ")
print("")

#procesamiento y condiciones

edad = (2022-nac)

civil = civil.upper()
sector = sector.upper ()

if años > 10 and hijos >= 2:
    print("APORBADO")

elif civil == "C" and hijos > 3 and edad > 45 and edad < 55:
    print("APROBADO")

elif ing >= 2500000 and civil == "S" and sector == "U":
    print("APROBADO")

elif ing >= 3500000 and años > 5:
    print("APROBADO")

elif sector == "R" and civil == "C" and hijos < 2:
    print("APROBADO")

else:
    print("RECHAZADO")


