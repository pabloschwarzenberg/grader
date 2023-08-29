#Aprobación de créditos
ingreso = int(input("ingreso: "))
nacimiento = int(input("nacimiento: "))
hijos = int(input("hijos: "))
tiempo = int(input("tiempo en el banco: "))
civil = str(input("Estado civil: "))
vivienda = str(input("¿donde vive?: "))

ano = 2020 - nacimiento

if ( tiempo > 10 and hijos >= 2):
    print("el resultado debe ser APROBADO")
elif( civil == "C" and hijos > 3 and ( ano >= 45 and ano <= 55) ):
    print("el resultado debe ser APROBADO")
elif( ingreso > 2500000 and civil == "S" and vivienda == "U"):
    print("el resultado debe ser APROBADO")
elif( ingreso > 3500000 and tiempo > 5):
    print("el resultado debe ser APROBADO")
elif( vivienda == "R" and civil == "C" and hijos < 2):
    print("el resultado debe ser APROBADO")
else:
    print("el resultado debe ser RECHAZADO")