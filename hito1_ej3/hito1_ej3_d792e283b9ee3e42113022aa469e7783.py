#Aprobación de créditos
Ingreso = int(input("Ingreso en pesos: "))
Año_de_nacimiento = int(input("Año de Nacimiento: "))
Num_hijos = int(input("Numero de hijos: "))
Años_pert = int(input("Años perteneciencia al banco: "))
Estado_civil = str(input("S: soltero, C, casado:"))
Donde_vive = str(input("U: urbano, R: rural: "))

if Años_pert > 10 and Num_hijos > 2 :
    print( "APROBADO")
elif Estado_civil == "C" and Num_hijos > 3 and (Año_de_nacimiento-2021) >45 and (Año_de_nacimiento-2021)<55:
    print( "APROBADO")
elif Ingreso > 2500000 and Estado_civil=="S" and Donde_vive =="U":
    print( "APROBADO")
elif Ingreso > 3500000 and Años_pert > 5:
    print( "APROBADO")
elif Donde_vive =="R" and Estado_civil =="C" and Num_hijos <=2:
    print( "APROBADO")
else: print( "RECHAZADO")