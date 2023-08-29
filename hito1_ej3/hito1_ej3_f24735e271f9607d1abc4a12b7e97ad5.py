#Aprobación de créditos
ingreso = int(input("Ingreso:"))
nacimiento = int(input("Ingresa año de nacimiento:"))
nacimiento = nacimiento - 2023
numdehijos = int(input("Ingresa numero de hijos:"))
pertbanco =int(input("Ingresa años de pertenencia al banco:"))
estado = str(input("Ingresa estado civil:"))
campOciud = str(input("Vives en campo o ciudad(U = urbano,R = rural):"))
if pertbanco >= 10 and numdehijos >= 2:
    resultado = "APROBADO"
elif estado == "S" and numdehijos >=3 and nacimiento >= 45 and nacimiento <= 55:
    resultado = "APROBADO"
elif ingreso >= 2500000 and estado == "S" and campOciud == "U":
    resultado = "APROBADO"
elif ingreso >= 3500000 and pertbanco >= 5:
    resultado = "APROBADO"
elif campOciud == "R" and estado == "C" and numdehijos <= 2:
    resultado = "APROBADO"
else:
    resultado = "RECHAZADO"

print(resultado)      