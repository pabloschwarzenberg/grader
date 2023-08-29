#Aprobación de créditos
ingreso = int(input("Ingrese el ingreso mensual en pesos: "))
nacimiento = int(input("Ingrese su edad: "))
hijos = int(input("Ingrese cantidad de hijos: "))
pertenencia = int(input("Ingrese los años de pertenencia a la empresa: "))
estadocivil = input("Ingrese su estado civil (S para soltero, C para casado): ")
ubi = input("Ingrese la ubicacion (U para urbano, R para rural: ")

if pertenencia > 10 and hijos >= 2:
    resultado = "APROBADO"
    
elif estadocivil == "C" and hijos > 3 and nacimiento >= 45 and nacimiento <= 55:
    resultado = "APROBADO"
    
elif ingreso > 2500000 and estadocivil == "S" and ubi == "U":
    resultado = "APROBADO"

elif ingreso > 3500000 and pertenencia < 5:
    resultado = "APROBADO"

elif ubi == "R" and estadocivil == "C" and hijos < 2:
    resultado = "APROBADO"

else:
    resultado = "RECHAZADO"
  
print(resultado)