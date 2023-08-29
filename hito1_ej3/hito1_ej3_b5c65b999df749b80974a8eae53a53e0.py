#Aprobación de créditos
ingreso = int(input("Coloque aquí su ingreso (en pesos): "))
edad = int(input("Coloque aquí su edad: "))
hijos = int(input("Coloque aquí el número de hijos que tiene: "))
años = int(input("Coloque aquí cuantos años de pertenencia tiene en el banco: "))
est_civil = input("Coloque aquí su estado civil (S: Soltero ; C: Casado): ")
vive = input("Coloque aquí si vive en campo o ciudad (U: Urbano ; R: Rural): ")

if años > 10 and hijos >= 2:
    print("APROBADO")
elif est_civil == "C" and hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and est_civil == "S" and vive == "U":
    print("APROBADO")
elif ingreso > 3500000 and años > 5:
    print("APROBADO")
elif vive == "R" and est_civil == "C" and hijos < 3:
    print("APROBADO")
else:
    print("RECHAZADO")      