#Aprobación de créditos
Ingresos= int(input("Ingresos(en pesos): "))
Año= int(input("Año de nacimiento: "))
hijos= int(input("Numero de hijos: "))
pertenencia= int(input("Años de pertenencia al banco: "))
civil= str(input("Estado civil(S:soltero, C:casado) "))
vivir= str(input("vivienda, campo o ciudad(U:urbano, R:rural)" ))
resultado = "RECHAZADO"

if pertenencia > 10 and hijos >=2:
    resultado = "APROBADO"
if civil == "C" and hijos > 3 and 45 <= Año >= 55:
    resultado = "APROBADO"
if Ingresos >= 2500000 and civil == "S" and vivir == "U":
    resultado = "APROBADO"
if Ingresos >= 3500000 and pertenencia > 5:
    resultado = "APROBADO"
if vivir == "R" and civil == "C" and hijos < 2:
    resultado = "APROBADO"
print(resultado)      