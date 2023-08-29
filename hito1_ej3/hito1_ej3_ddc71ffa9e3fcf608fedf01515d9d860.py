#Aprobación de créditos
ingreso = int(input("Ingresos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
aniosp = int(input("Años de pertenencia del banco: "))
estado = str(input("Estado civil: "))
zona = str(input("Campo (R) o ciudad (U): "))

edad = 2023 - nacimiento

resultado = "RECHAZADO"

if aniosp > 10 and hijos >= 2:
    resultado = "APROBADO"

elif estado == "C" and hijos > 3 and 45 <= edad <= 55:
    resultado = "APROBADO"

elif ingreso > 2500000 and estado == "S" and zona == "U":
    resultado = "APROBADO"

elif ingreso > 3500000 and aniosp > 5:
    resultado = "APROBADO"

elif zona == "R" and estado == "C" and hijos < 2:
    resultado = "APROBADO"

print(resultado)