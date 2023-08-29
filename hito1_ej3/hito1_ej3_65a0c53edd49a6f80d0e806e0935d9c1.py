I = int(input("Ingreso: "))
AdN = int(input("Año de nacimiento: "))
NdH = int(input("Número de hijos: "))
AdPB = int(input("Años de pertenencia al banco: "))
EC = input("Estado Civil (S/C): ")
UR = input ("Zona urbana o rural (U/R): ")
Edad = 2023 - AdN

if AdPB > 10 and NdH >= 2:
    print("APROBADO")
elif EC == "C" and 45 < Edad < 55 and NdH > 3:
    print("APROBADO")
elif I > 2500000 and EC == "S" and UR == "U":
    print("APROBADO")
elif I > 3500000 and AdPB > 5:
    print("APROBADO")
elif UR == "R" and EC == "C" and NdH < 2:
    print("APROBADO")
else:
    print("REPROBADO")