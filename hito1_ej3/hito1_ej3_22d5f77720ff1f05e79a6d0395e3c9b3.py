#Aprobacion de creditos
ingresos = eval(input("Ingrese monto de sus ingresos: "))
ano = eval(input("Ingrese su año de nacimiento: "))
hijos = eval(input("Ingrese la cantidad de hijos: "))
pertenencia = eval(input("Ingrese años de pertenencia con el banco: "))
estado_civil = input("Ingrese su estado civil: ")
donde_vive = input("Ingrese donde vive: ")

edad = 2021-ano

if (pertenencia>10) and (hijos>=2):
    print("APROBADO")
elif (estado_civil== "C") and (hijos>3) and (edad>45) and (edad<55):
    print("APROBADO")
elif (ingresos>=2500000) and (estado_civil=="S") and (donde_vive=="U"):
    print("APROBADO")
elif (ingresos>=3500000) and (pertenencia>5):
    print("")
elif (donde_vive=="R") and (estado_civil=="C") and (hijos<2):
    print("APROBADO")
else:
    print("Credito Denegado")