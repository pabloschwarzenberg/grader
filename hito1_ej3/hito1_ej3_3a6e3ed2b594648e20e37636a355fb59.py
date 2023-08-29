#Aprobación de créditos
ingresos = int(input("Ingrese la cantidad de sus ingresos(CLP):"))
nacimiento = int(input("Ingrese año de nacimiento:"))
hijos = int(input("Ingrese su cantidad de hijos:"))
antiguedad = int(input("Ingrese sus años de antiguedad en el banco:"))
print("Ingrese su estado civil (soltero o casado) S o C")
solterocasado = str(input("[S] o [C]:"))
print("Ingrese localidad de su vivienda (urbano o rural)")
localidad = str(input("[U] o [R]:"))
if antiguedad > 10 and hijos >=2:
    print("APROBADO")
elif solterocasado == "C" and hijos > 3 and (2021 - nacimiento >= 45) and (2021 - nacimiento <=55):
    print("APROBADO")
elif ingresos > 2500000 and solterocasado == "S" and localidad == "U":
    print("APROBADO")
elif ingresos > 3500000 and antiguedad > 5:
    print("CREDITO APROBADO")
elif solterocasado == "C" and localidad == "R" and hijos < 2:
    print("CREDITO APROBADO")
else:
    print("CREDITO RECHAZADO")      