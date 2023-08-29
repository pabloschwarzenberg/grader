#Aprobación de créditos
ingreso = int(input("Ingrese su ingreso (en pesos): "))
nacimiento = int(input("Ingrese el año de nacimiento: "))
hijos = int(input("Ingrese el número de hijos: "))
banco = int(input("Ingrese los Años en el banco: "))
estado = str(input("Ingrese Estado Civil (S: Soltero, C: Casado): "))
lugar = str(input("Ingrese lugar en que vive (R: Rural, U: Urbano): "))
edad = 2021 - nacimiento

if banco >= 10 and hijos >= 2:
    x = "APROBADO"
elif (estado == "C") and (hijos >= 3) and (45 < edad < 55):
    x = "APROBADO"
elif (ingreso >= 2500000) and (estado == "S") and (lugar == "U"):
    x = "APROBADO"
elif (ingreso >= 3500000) and (banco >= 5):
    x = "APROBADO"
elif (lugar == "R") and (estado == "C") and (hijos < 2):
    x = "APROBADO"
else:
    x = "REPROBADO"
print ("Su crédito esta:", (x))
