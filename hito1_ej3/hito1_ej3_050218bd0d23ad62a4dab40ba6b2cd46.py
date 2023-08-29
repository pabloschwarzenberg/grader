 #Aprobación de créditos

Ingresos = int(input(" Ingrese sus Ingresos en pesos: " ))

Año_de_nacimiento = int(input(" Ingrese su año de nacimiento: " ))

Número_de_hijos = int(input(" Ingrese número de hijos: " ))

Años_banco = int(input(" Ingrese cuantos años lleva en el banco: " ))

Estado_civil = str(input(" Ingrese si es soltero (S) o casado (C): " ))

Vivienda = str(input(" Ingrese si vive en un lugar urbano (U) o rural (R): " ))

Años = 2022 - Año_de_nacimiento


if Años_banco > 10 and Número_de_hijos >= 2:
    print("APROBADO")

elif Estado_civil == "C" and Número_de_hijos > 3 and 55 >= Años >= 45:
    print("APROBADO")
elif Ingresos > 2500000 and Estado_civil == "S" and Vivienda == "R":
    print("APROBADO")
elif Ingresos > 3500000 and Años_banco > 5:
    print("APROBADO")
if Vivienda == "R" and Estado_civil == "C" and Número_de_hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")