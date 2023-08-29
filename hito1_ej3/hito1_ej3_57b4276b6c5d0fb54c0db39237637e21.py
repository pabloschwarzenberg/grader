#Aprobación de créditos

ingreso = int(input("Cuál es su ingreso mensual? :"))
nacimiento = int(input("Ingrese su año de nacimiento: "))
numeroDeHijos = int(input("Ingrese número de hijos: "))
pertenencia = int(input("Ingrese número de años desde su ingreso al banco: "))
estadoCivil = input("Ingrese su estado civil: ")
tipoDeLugarDondeVive = input("Ingrese si vive en campo o ciudad: ")

edad = 2020 - nacimiento

if pertenencia > 10 and numeroDeHijos >= 2:
    print("APROBADO")
elif estadoCivil == "C" and numeroDeHijos > 3 and 45 <= edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estadoCivil == "S" and tipoDeLugarDondeVive == "U":
    print("APROBADO")
elif ingreso > 3500000 and pertenencia > 5:
    print("APROBADO")
elif tipoDeLugarDondeVive == "R" and estadoCivil == "C" and numeroDeHijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")