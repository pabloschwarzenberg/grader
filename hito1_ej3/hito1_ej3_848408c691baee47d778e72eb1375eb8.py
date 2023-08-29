Ingresos= int(input("Ingreso (en pesos):"))

Ano = int(input("Año de nacimiento:"))

Hijos = int(input("Número de hijos:"))

Antiguedad = int(input("Años de pertenencia al banco:"))

CasSol = str(input("Estado civil (S: soltero, C, casado):"))

Urbaral = str(input("Si vive en campo o cuidad (U: urbano, R: rural):"))

if Antiguedad > 10 and Hijos >=2:
    print("APROBADO")
    
elif CasSol == "C" and Hijos > 3 and (2021 - Ano >= 45) and (2021 - Ano <=55):
    print("APROBADO")
    
elif Ingresos > 2500000 and CasSol == "S" and Urbaral == "U":
    print("APROBADO")
    
elif Ingresos > 3500000 and Antiguedad > 5:
    print("APROBADO")
    
elif CasSol == "C" and Urbaral == "R" and Hijos < 2:
    print("APROBADO")
    
else:
    print("RECHAZADO")