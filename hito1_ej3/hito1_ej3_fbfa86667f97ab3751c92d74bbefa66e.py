#Aprobación de créditos
ingresos = int(input("dame tus ingresos: "))
ano = int(input("dame tu añod e nacimiento"))
hijos = int(input("dame la cantidad de hijos que tienes"))
pertenencia = int(input("dame tus años de pertenencia al banco: "))
estado = input("S para soltero y C para Casado: ")
vivienda = input("U para urbano y R para rural: ")
edad = 2022-ano

if pertenencia > 10 and hijos > 2:
    print("APROBADO")
elif estado == "C" and hijos < 3 and 45 < edad < 55:
    print("APROBADO")
elif ingresos > 2500000 and estado == "S" and vivienda == "U":
    print("APROBADO")
elif ingresos > 3500000 and pertenencia > 5:
    print("APROBADO")
elif vivienda == "R" and estado == "C" and hijos < 2:
    print("APROBADO")
