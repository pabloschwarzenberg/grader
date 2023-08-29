#Aprobación de créditos
ingresos = eval(input("Ingrese sus ingresos en CLP "))
nacimiento = eval(input("Ingrese su año de Nacimiento "))
nro_hijos = eval(input("Indique cuántos hijos tiene "))
pertenencia = eval(input("Indique cuántos años de pertenencia al banco tiene "))
estado_civil = input("Indique su Estado Civil ")
residencia = input("Indique si vive en Campo o Ciudad ")
edad = 2021 - nacimiento
if pertenencia > 10 and nro_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and nro_hijos > 3 and 55 >= edad >= 45:
    print("APROBADO")
elif ingresos > 2500000 and estado_civil == "S" and residencia == "R":
    print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
elif residencia == "R" and estado_civil == "C" and nro_hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")