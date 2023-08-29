#Aprobación de créditos
ingresos = int(input("Ingrese los ingresos que usted recibe: "))
year = int(input("Ingrese su año de nacimiento: "))
numeroh = int(input("Ingrese el numero de hijos que tiene: "))
apb = str(input("Ingrese los años que lleva en el banco: "))
estadoc = str(input("Ingrese su estado civil: "))
vive = str(input("Ingrese si vive en el campo o ciudad: "))

edad = 2022 - year

C = "casado" or "Casado"
S = "soltero" or "Soltero"
U = "ciudad" or "Ciudad"
R = "campo" or "Campo"

if apb > "10" or numeroh > "2":
    print("APROBADO")

elif estadoc == C or numeroh > "3" or edad >= "45":
    print("APROBADO")

elif ingresos > "2500000" or estadoc == S or vive == U:
    print("APROBADO")

elif ingresos > "3500000" or apb >= "5":
    print("APROBADO")

elif vive == R or estadoc == C or numeroh < "2":
    print("APROBADO")
else:
    print("RECHAZADO")