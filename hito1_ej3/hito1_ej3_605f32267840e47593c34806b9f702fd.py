#Aprobación de créditos
ingresos = int(input("¿Cuanto son sus ingresos?(en pesos): "))
aNacimiento = int(input("Ingrese su AÑO de nacimiento: "))
nHijos = int(input("¿Cuantos hijos tiene?: "))
aBanco = int(input("¿Cuantos años de pertenencia tiene en nuestro banco?: "))
eCivil = str(input("Estado civil ('S': soltero, 'C', casado): "))
residencia = str(input("Si vive en campo o cuidad ('U': urbano, 'R': rural): "))
edad = 2021 - aNacimiento

if (aBanco > 10 and nHijos >= 2):
    print("APROBADO")
elif (eCivil == "C" or eCivil == "c") and (edad >= 45 and edad <= 55) and (nHijos > 3):
    print("APROBADO")
elif (ingresos > 2500000) and (eCivil == "c" or eCivil == "C") and (residencia == "u" or residencia == "U"):
    print("APROBADO")
elif (ingresos > 3500000) and (aBanco > 5): 
    print("APROBADO")
elif (residencia == "r" or residencia == "R") and (eCivil == "c" or eCivil == "C") and (nHijos < 2):
    print("APROBADO")
else:
    print("RECHAZADO")