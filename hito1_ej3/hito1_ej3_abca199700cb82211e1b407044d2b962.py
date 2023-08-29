#Aprobación de créditos
E = int(input("Ingrese su año de nacimiento: "))
hijos = int(input("Ingrese la cantidad de hijos: "))
banco = int(input("Ingrese los años que usted está en el banco: "))
ingresos = int(input("Coloque sus ingresos en pesos: "))
civil = str(input("Ingrese su estado civil: ")) 
vivir = str(input("Ingrese donde vive: "))

edad = 2021 - E


if (banco > 10 and hijos >= 2):
    print("APROBADO")
elif (banco <= 10 and hijos < 2):
    print("RECHAZADO")
if (civil == "casado" and hijos > 3 and edad >= 45 or edad <= 55):
    print("APROBADO")
elif (civil!= "casado" and hijos < 2 and edad < 45 or edad > 55):
    print("RECHAZADO")
if (ingresos > 2500000 and civil == "soltero" and vivir == "urbano"):
    print("APROBADO")
elif ingresos < 2500000 and civil != "soltero" and vivir != "urbano":
    print("RECHAZADO")
if (ingresos > 3500000 and banco > 5):
    print("APROBADO")
elif ingresos < 3500000 and banco < 5:
    print("RECHAZADO")