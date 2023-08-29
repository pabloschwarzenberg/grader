#Aprobación de créditos
ingreso_pesos= int(input("Ingreso en pesos: "))
naci_miento= int(input("Su año de nacimiento: "))
num_hijos= int(input("Numero de hijos: "))
perte_nencia= int(input("Años de pertenecia al banco: "))
cas_sol= str(input("Estado civil: "))
zo_na= str(input("Vive en zona Urbana o Rural: "))

if (10 < perte_nencia)and (2 <= num_hijos):
    print("APROBADO")
elif(cas_sol == "C")and (3 < num_hijos) and (1965 < naci_miento < 1977):
    print("APROBADO")
elif(2500000 < ingreso_pesos)and (cas_sol == "S")and (zo_na == "U"):
    print("APROBADO")  
elif (3500000 < ingreso_pesos) and (5 < perte_nencia):
    print("APROBADO")
elif (zo_na == "R") and (cas_sol == "C")and (num_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")     