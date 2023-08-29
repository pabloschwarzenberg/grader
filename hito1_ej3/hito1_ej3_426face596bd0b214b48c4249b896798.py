#Aprobación de créditos

ingreso = int(input("Ingreso (en pesos): "))
ano_nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("Numero de hijos: "))
pertenece = int(input("Años de pertenencia al banco: "))
estado_civil = str(input('Estado civil ("S":soltero/a, "C":casado/a) : '))
vive_en = str(input('Si vive en campo o ciudad ("U":urbano, "R":rural) : '))

edad = 2021 - ano_nacimiento

resultado = "RECHAZADO"

if (pertenece > 10 and hijos >= 2) or (estado_civil == "C" and hijos > 3 and edad >=45 and edad <= 55) or (ingreso > 2500000 and estado_civil == "S" and vive_en == "U") or (ingreso > 3500000 and pertenece > 5) or (vive_en == "R" and estado_civil == "C" and hijos < 2):
  resultado = "APROBADO"

print("Credito: ", resultado)






