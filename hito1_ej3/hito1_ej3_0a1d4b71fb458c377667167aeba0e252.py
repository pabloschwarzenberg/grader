
renta = int(input("Ingreso (en pesos): "))
nacimiento = int(input("Año de nacimiento: "))
hijoscantidad = int(input("Número de hijos: "))
bancoedad = int(input("Años de pertenencia al banco: "))
estadocivil= input("Estado civil ('S': soltero, 'C': casado): ")
Ubicacion = input("Si vive en campo o cuidad ('U': urbano, 'R': rural): ")
age = 2023 - nacimiento
            
if bancoedad > 10 and hijoscantidad >= 2:
                print("APROBADO")
elif estadocivil == "C" and hijoscantidad > 3 and 45 <= age <= 55:
                print("APROBADO")
elif renta > 2500000 and estadocivil == "S" and Ubicacion == "U":
                print("APROBADO")
elif renta > 3500000 and bancoedad > 5:
                print("APROBADO")
elif Ubicacion == "R" and estadocivil == "C" and hijoscantidad < 2:
                print("APROBADO")
else:
                print("RECHAZADO")