#Aprobación de créditos
Ingreso = int(input("Ingrese sus ingresos: "))
nacimiento = int(input("Ingrese su edad: "))
hijos = int(input("Ingrese numero de hijos: "))
pertenencia = int(input("Ingrese años de pertenencia al banco: "))
estado = str(input("Ingrese estado civil (S:soltero, C: casado): "))
lugar = str(input("Ingrese donde vive (U:urbano,R:rural): "))
if pertenencia > 10 and hijos >=2:
   resultado = "APROBADO"
elif estado == "C" and hijos > 3 and 45 <= (2023 - nacimiento) and nacimiento <= 55:
   resultado = "APROBADO"
elif Ingreso > 2500000 and estado == "S" and lugar == "U":
    resultado = "APROBADO"
elif Ingreso > 3500000 and pertenencia > 5:
   resultado = "APROBADO"
elif lugar == "R" and estado == "C" and hijos < 2:
   resultado = "APROBADO"
else:
   resultado = "RECHAZADO"
print(resultado)     