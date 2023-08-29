ingreso = int(input())
a_nacimiento = int(input())
edad = 2022 - a_nacimiento
num_hijos = int(input())
a_presencia_banco = int(input())
estado_civil = input()
lugar_recidencia = input()


if a_presencia_banco >= 10 and num_hijos >= 2:
    print("APROBADO")
elif estado_civil == "C" and num_hijos > 3 and edad >= 45 and edad <= 55:
    print("APROBADO")
elif ingreso > 2500000 and estado_civil == "S" and lugar_recidencia == "U":
    print("APROBADO")
elif ingreso > 3500000 and a_presencia_banco > 5:
    print("APROBADO")
elif lugar_recidencia == "R" and estado_civil == "C" and num_hijos < 2:
    print("APROBADO")
else:
    print ("RECHAZADO")