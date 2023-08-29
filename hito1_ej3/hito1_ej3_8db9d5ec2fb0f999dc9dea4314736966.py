#Aprobación de créditos
def credito(ingreso,edad,numhijos,añosbanco,e_civil,vive):
    if añosbanco > 10 and numhijos >= 2:
        return "APROBADO"
    elif e_civil == "C" and numhijos > 3 and 45 <= (2023 - edad) <= 55:
        return "APROBADO"
    elif ingreso > 2500000 and e_civil == "S" and vive == "U":
        return "APROBADO"
    elif ingreso > 3500000 and añosbanco > 5 and numhijos < 2: 
        return "APROBADO"
    elif vive == "R" and e_civil == "C" and numhijos < 2:
        return "APROBADO"  
    else: 
        return "REPROBADO"
    
ingreso = int(input("Ingreso(en pesos): "))
edad = int(input("Año de nacimiento: "))
numhijos = int(input("Número de hijos: "))
añosbanco = int(input("Años de pertenencia al banco: "))
e_civil = str(input('Estado civil ("S": soltero, "C", casado): '))
vive = str(input('Si vive en campo o cuidad ("U": urbano, "R": rural): '))
e_civil = e_civil.upper()
vive = vive.upper()
print("Su credito ha sido",credito(ingreso,edad,numhijos,añosbanco,e_civil,vive))

