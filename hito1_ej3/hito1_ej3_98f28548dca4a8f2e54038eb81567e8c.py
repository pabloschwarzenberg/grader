#Aprobación de créditos
ing = int(input(("Ingrese su salario en pesos: $")))
anio = int(input(("Ingrese su año de nacimiento: ")))
hijos = int(input(("Ingrese su cantidad de hijos: ")))
anio_banc = int(input(("Ingrese los años que lleva en el banco: ")))
est_civil = str(input(("Ingrese su estado civil (S - Soltero, C - Casado): ")))
vivienda = str(input(("Ingrese su residencia donde: U - Urbano, R - Rural): ")))
edad = 2021 - anio

if anio_banc > 10 and hijos >=2:
    print("APROBADO")

if est_civil == "C" and hijos >= 3 and edad >= 45 and edad <=55:
    print("APROBADO")

if ing > 2500000 and est_civil >= "S" and vivienda == "U":
    print("APROBADO")

if ing > 3500000 and anio_banc >= 5:
    print("APROBADO")

if vivienda == "R" and est_civil == "C" and hijos < 2:
    print("APROBADO")

print("RECHAZADO")