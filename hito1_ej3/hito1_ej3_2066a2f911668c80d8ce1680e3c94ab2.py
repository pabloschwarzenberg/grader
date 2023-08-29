#Aprobación de créditos
ingresos = int(input("Indique su ingreso(en pesos: "))
nacimiento = int(input("Indique su año de nacimiento: "))
hijos = int(input("Ingrese numero de hijos: "))
pertenencia_banco = int(input("Indique años de pertenencia al banco"))
estado_civil = str(input("Indique su estdo civil: "))
campo_ciudad = str(input("Indique si vivi en campo o ciudad: "))
edad = 2023 - nacimiento

if pertenencia_banco > 10 and hijos >= 2:
    print("Credito APROBADO")

elif estado_civil == "C" and hijos > 3 and 45 < edad < 55:
    print("Credito APROBADO")

elif ingresos > 2500000 and estado_civil == "S" and campo_ciudad == "U":
    print("Credito APROBADO")

elif ingresos > 3500000 and pertenencia_banco > 5:
    print("Credito APROBADO")
    
elif campo_ciudad == "R" and estado_civil == "C" and hijos < 2:
    print("Credito APROBADO")

else:
    print("Credito RECHAZADO")     