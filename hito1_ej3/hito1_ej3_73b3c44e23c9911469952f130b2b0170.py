#Aprobación de créditos
print("---------------------------------------")
print("Bienvenido a la postulación de créditos")
print("---------------------------------------")
print("     Ingrese los siguientes datos")
print("---------------------------------------")

# INPUTS

Ingreso = int(input("Escriba sus ingresos:\n"))
Nacimiento = int(input("Año de nacimiento:\n"))
Hijos = int(input("Cuantos hijos tiene:\n"))
Años = int(input("Cuantos años lleva en el banco:\n"))
Estado = input("Estado civil (S o C):\n")
Residencia = input("¿Vive en zona campo o ciudad?(U o R)\n")

Edad = 2022-Nacimiento

# if y elif

if (Años > 10) and (Hijos >= 2):
    print("APROBADO")
elif (Estado == "C") and (Hijos > 3) and (Edad >= 45) and (Edad <=55):
    print("APROBADO")
elif (Ingreso > 2500000) and (Estado == "S") and (Residencia == "C"):
    print("APROBADO")
elif (Ingreso > 3500000) and (Años > 5):
    print("APROBADO")
elif (Residencia == "R") and (Estado == "C") and (Hijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")