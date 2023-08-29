#Aprobación de créditos
ingreso = int(input("cantidad de ingreso (en pesos): "))
a_nacimiento = int(input("ingrese el año de nacimiento: "))
edad = 2023 - a_nacimiento
n_hijos = int(input("ingrese cantidad de hijos/as: "))
a_banco = int(input("ingrese cantidad de años de pertenecia al banco: "))
e_civil = input("ingrese estado civil (S = soltero / C = casado): ")
d_vive = input("ingrese zona (R = rural / U = urbano): ")

if (a_banco > 10) and (n_hijos >= 2):
    print("APROBADO")
elif (e_civil == "C") and (n_hijos > 3) and (45 <= edad <= 55):
    print("APROBADO")
elif (ingreso > 2500000) and (e_civil == "S") and (d_vive == "U"):
    print("APROBADO")
elif (ingreso > 3500000) and (a_banco > 5):
    print("APROBADO")
elif (d_vive == "R") and (e_civil == "C") and (n_hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")      