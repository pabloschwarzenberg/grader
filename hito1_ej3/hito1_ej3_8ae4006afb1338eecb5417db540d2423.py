#Aprobación de créditos

ingreso = int (input ("ingrese sus ingresos: "))
ano_nacimiento = int (input ("ingrese su año de nacimiento: "))
numero_hijos = int (input ("ingrese el numero de hijos que tiene: "))
antiguedad_banco = int (input ("ingrese sus años de antiguedad en el banco: "))
estado_civil = input ("Soltero (S) o Casado (C): ")
vivienda = input ("Usted vive campo (R) o ciudad (U): ")

edad = 2022 - ano_nacimiento

if (antiguedad_banco >= 10) and (numero_hijos >= 2): 
    print ("APROBADO")
elif (estado_civil == "C") and (numero_hijos > 3) and (edad >= 45 and edad <= 55):
    print ("APROBADO")
elif (ingreso > 2500000) and (estado_civil == "S") and (vivienda == "U"):
    print ("APROBADO")
elif (ingreso > 3500000) and (antiguedad_banco > 5):
    print ("APROBADO") 
elif (vivienda == "R") and (estado_civil == "C") and (numero_hijos < 2):
    print ("APROBADO")
else: 
    print ("RECHAZADO")