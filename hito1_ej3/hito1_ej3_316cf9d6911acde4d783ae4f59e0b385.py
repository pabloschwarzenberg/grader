#Aprobación de créditos
#Aprobación de créditos
Ingresos = int(input("ingresos (en pesos) :  "))
Año_de_nacimiento = int(input("año de nacimiento:  "))
Numero_de_hijos = int(input("numero de hijos: "))
Años_banco = int(input("años de pertenencia al banco:  "))
Estado_civil = input("estado civil (S: soltero, C: casado):  ")
urbano_ciudad = input("Si vive en campo o cuidad (U: urbano, R: rural):  ")

if Años_banco >= 10 and Numero_de_hijos >= 2:
    print("APROBADO")

elif Estado_civil == "C" and Numero_de_hijos > 3 and Año_de_nacimiento >= 45 and Año_de_nacimiento < 56:
    print("APROBADO")

elif Ingresos > 2500000 and Estado_civil == "S" and urbano_ciudad == "U":
    print("APROBADO")

elif Ingresos > 3500000 and Años_banco > 5:
    print("APROBADO")

elif urbano_ciudad == "R" and Estado_civil == "C" and Numero_de_hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")