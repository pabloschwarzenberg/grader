#Aprobación de créditos
pesos = (int(input("ingreso: ")))
anos_de_nacimiento = (input("fecha de nacimiento: "))
hijos = (int(input("numero de hijos: ")))
anos_de_pertenencia_al_banco = (input("años de pertenencia "))
estado_civil = (input("estado civil: "))
localidad = (input("lugar donde vive: "))
aprobado = False

while estado_civil != "s" and estado_civil != "c":
    estado_civil = input("estado civil: ")
while localidad != "U" and localidad != "R":
    localidad = input("lugar donde vive")

if  anos_de_pertenencia_al_banco >= "10" and hijos >= 2:
    aprobado = True  
if estado_civil == "c" and hijos > 3 and anos_de_nacimiento <= 45 and anos_de_nacimiento >= 55:
    aprobado: True
if pesos > 2500000 and estado_civil == "s" and localidad == "U":
    aprobado = True 
if pesos > 3500000 and anos_de_pertenencia_al_banco > "5":
    aprobado = True
if localidad == "R" and estado_civil == "c" and hijos > 2:
    aprobado:True
if aprobado:
    print("APROBADO")
else:
    print("RECHAZADO")