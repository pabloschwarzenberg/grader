#Aprobación de créditos
ingresos = int(input("Ingrese el monto de sus ingresos :"))
nacimiento = int(input("Ingrese el año de nacimiento:"))
edad = 2020-nacimiento
hijos = int(input("Ingrese el número de hijos:"))
pertenencia = int(input("Ingrese la cantidad de años en el banco:"))
estado = str(input("Ingrese su estado civil:"))
residencia = str(input("Ingrese lugar de residencia:"))
edad = 2020-nacimiento
if (pertenencia>10) and (hijos>=2):
    print("APROBADO")

elif(estado == "C")and(hijos > 3)and (45 >= edad <= 55):
    print("APROBADO")

elif (ingresos > 2500000) and (estado == "S") and (residencia == "U"):
    print("APROBADO")

elif (ingresos > 3500000)and (pertenencia > 5):
    print("APROBADO")

elif (residencia == "R")and(estado == "C")and(hijos < 2):
    print("APROBADO")
else:
     print("RECHAZADO")
