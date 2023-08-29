#Aprobación de créditos
ingresos = int(input("Ingresar su total de ingresos: "))
ano_nacimiento = int(input("Ingresar año de nacimiento: "))
num_hijos = int(input("Ingresar cantidad de hijos: "))
tiempo_banco = int(input("Ingresar su trayectoria en el banco: "))
estado_civil = input("Ingresar 'S' si esta soltero/a y 'C' si esta casado/a: ")
localidad = input("Ingresar 'R' si es de zona rural y 'U' si es zona urbana: ")

if tiempo_banco >= 10 and num_hijos >= 2:
    print("APROBADO")
else:
    print("RECHAZADO")
if estado_civil == "C":
    if num_hijos > 3 and 1978 < ano_nacimiento > 1968:
        print("APROBADO")
    else:
        print("RECHAZADO")
if ingresos > 2500000:
    if estado_civil == "S" and localidad == "U":
        print("APROBADO")
    else:
        print("RECHAZADO")
if ingresos > 3500000 and tiempo_banco > 5:
    print("se acepta el credito")
else:
    print("RECHAZADO")
if localidad == "R":
    if estado_civil == "C" and num_hijos < 2:
        print("APROBADO")
    else: 
        print("RECHAZADO")
