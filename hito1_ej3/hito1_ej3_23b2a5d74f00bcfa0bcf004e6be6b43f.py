#Aprobación de créditos
ingresos = int(input("Ingresos: "))
nacimiento = int(input("Año de nacimiento: "))
hijos = int(input("N° de hijos"))
tiempo_afiliacion = int(input("Años de pertenencia al banco: "))
estado_civil = eval(input("Estado civil  soltero,  casado"))
dondevive = eval(input("Si vive en campo o cuidad (U: urbano, R: rural) "))

if (tiempo_afiliacion >= 10) and (hijos >= 2):
    print("APROBADO")
elif estado_civil == 'C' and hijos > 3 and (nacimiento >= 45 or nacimiento <= 55 ):
    print("APROBADO")
elif ingresos > 2500000 and estado_civil == 'S' and dondevive == 'U':
    print("APROBADO")
elif ingresos > 3500000 and tiempo_afiliacion > 5:
    print("APROBADO")
elif dondevive == 'R' and estado_civil == 'C' and hijos < 2:
    print("APROBADO")
else:
    print("RECHAZADO")     